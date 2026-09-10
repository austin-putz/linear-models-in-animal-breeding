--[[
  {{< animation STEM caption="ONE SENTENCE" >}}

  Resolves assets/video/STEM.{mp4,png} and emits format-appropriate output:

    HTML  a <video> with the poster still, preload="none" so a chapter with
          five clips does not pull tens of MB before the reader scrolls.
    PDF   the poster still as an ordinary numbered figure, with the caption
          suffixed by a pointer to the HTML book.

  Why not Quarto's built-in {{< video >}}: tested on Quarto 1.9.37, in HTML it
  works, but in PDF it degrades to the literal text "t.mp4" — not a link, not a
  figure. Unusable for a book that ships a PDF.
--]]

local BOOK_URL = "https://austin-putz.github.io/linear-models-in-animal-breeding"

-- Paths in raw HTML are not rewritten by Quarto, so a chapter in chapters/
-- must reach up to the project root itself. quarto.project.offset is that
-- reach ("" at the root, ".." one level down).
local function root_prefix()
  local ok, offset = pcall(function()
    return quarto.project.offset
  end)
  if ok and offset ~= nil and offset ~= "" then
    return offset .. "/"
  end
  return ""
end

-- The URL is wrapped in \url{} before this runs, so its own characters are
-- left alone; everything else in a caption is ordinary prose.
local function escape_latex(s)
  local out = s:gsub("([&%%#%$])", "\\%1")
  out = out:gsub("_", "\\_")
  return out
end

local function escape_html(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
           :gsub('"', "&quot;"))
end

return {
  ["animation"] = function(args, kwargs)
    if args[1] == nil then
      error("animation shortcode: no asset stem given")
    end
    local stem = pandoc.utils.stringify(args[1])
    local cap = ""
    if kwargs["caption"] ~= nil then
      cap = pandoc.utils.stringify(kwargs["caption"])
    end

    local prefix = root_prefix()
    local mp4 = prefix .. "assets/video/" .. stem .. ".mp4"
    local png = prefix .. "assets/video/" .. stem .. ".png"

    -- NOTE: Quarto discovers <source src> but NOT the poster= attribute, and
    -- quarto.doc.add_resource() does not reach the book's resource collection
    -- from inside a shortcode. The poster stills are therefore shipped by the
    -- project-level `resources: assets/video/**` entry in _quarto.yml. If a
    -- video ever opens on a black frame in the deployed book, that entry is
    -- what has gone missing.

    if quarto.doc.is_format("html:js") then
      local html = table.concat({
        '<figure class="animation">',
        '<video controls muted playsinline preload="none" width="100%"',
        ' poster="', png, '">',
        '<source src="', mp4, '" type="video/mp4">',
        'Your browser cannot play this video. ',
        '<a href="', mp4, '">Download it instead.</a>',
        '</video>',
        (cap ~= "" and ('<figcaption>' .. escape_html(cap) .. '</figcaption>') or ''),
        '</figure>',
      })
      return pandoc.RawBlock("html", html)
    end

    -- Every other format (PDF, docx): the poster still as a numbered figure.
    --
    -- This is a raw LaTeX float rather than a pandoc Figure because Quarto's
    -- shortcode handler will not accept a Figure or a bare Para back from a
    -- shortcode -- both fail inside Quarto's own filter with "object has no
    -- __toinline metamethod". A raw float also avoids pandoc emitting
    -- \includegraphics[alt={...}], whose `alt` key is undefined in the book
    -- class and fails the build outright. LaTeX numbers it either way.
    -- Escape the author's caption first, then append the URL, so the \url{}
    -- we add is never itself mangled by the escaper.
    local print_cap = escape_latex(cap)
    if print_cap ~= "" then
      print_cap = print_cap .. " "
    end
    print_cap = print_cap .. "Animated in the web edition: \\url{" .. BOOK_URL .. "}"

    local latex = table.concat({
      "\\begin{figure}[htbp]\n",
      "\\centering\n",
      "\\includegraphics[width=0.92\\linewidth]{", png, "}\n",
      "\\caption{", print_cap, "}\n",
      "\\end{figure}\n",
    })
    return pandoc.RawBlock("latex", latex)
  end,
}
