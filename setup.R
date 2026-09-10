#!/usr/bin/env Rscript

# ============================================
# Setup script for Animal Models book
# Installs all required R packages
# ============================================

cat("Installing R packages for Animal Models book...\n\n")

# List of required CRAN packages
cran_packages <- c(
  # Document rendering
  "knitr",
  "rmarkdown",

  # Data manipulation and visualization
  "tidyverse",        # ggplot2, dplyr, tidyr, readr, etc.
  "here",            # Path management
  "glue",            # String interpolation

  # Mixed models
  "lme4",            # General mixed models
  "sommer",          # REML-based animal models
  "pedigreemm",      # Pedigree-based mixed models
  "MCMCglmm",        # Bayesian mixed models (MCMC)
  "coda",            # MCMC convergence diagnostics
  "survival",        # Survival analysis (Ch 15)
  "coxme",           # Cox models with random effects (Ch 15)

  # Matrix operations and pedigree
  "Matrix",          # Sparse matrices
  "nadiv",           # Numerical additive relationships
  "pedigree",        # Pedigree processing
  "orthopolynom",    # Legendre polynomials (Ch 12)
  "MASS",            # mvrnorm for multivariate normal

  # Tables and output
  "kableExtra",      # Beautiful HTML/LaTeX tables
  "gt",              # Grammar of tables
  "flextable",       # Cross-format tables

  # Plotting enhancements
  "patchwork",       # Combine ggplot2 plots
  "ggridges",        # Ridge plots for distributions
  "GGally",          # ggplot2 extensions (pairs plots)
  "scales",          # Scale functions for ggplot2
  "RColorBrewer"     # Color palettes
)

# Check which packages are already installed
installed <- installed.packages()[, "Package"]
to_install <- cran_packages[!cran_packages %in% installed]

if (length(to_install) > 0) {
  cat("Installing", length(to_install), "packages from CRAN:\n")
  cat(paste("-", to_install, collapse = "\n"), "\n\n")

  install.packages(
    to_install,
    dependencies = TRUE,
    repos = "https://cloud.r-project.org"
  )
} else {
  cat("All required packages are already installed.\n\n")
}

# Verify installation
cat("\nVerifying installation...\n")
missing <- cran_packages[!cran_packages %in% installed.packages()[, "Package"]]

if (length(missing) > 0) {
  cat("\nWARNING: The following packages failed to install:\n")
  cat(paste("-", missing, collapse = "\n"), "\n")
  cat("\nPlease install them manually:\n")
  cat("install.packages(c('", paste(missing, collapse = "', '"), "'))\n", sep = "")
  quit(status = 1)
} else {
  cat("\nAll packages installed successfully!\n")
  cat("\nYou can now render the book:\n")
  cat("  quarto render\n")
  cat("\nOr preview it:\n")
  cat("  quarto preview\n\n")
}

# Print package versions for debugging
cat("\n=== Package Versions ===\n")
for (pkg in cran_packages) {
  if (pkg %in% installed.packages()[, "Package"]) {
    version <- packageVersion(pkg)
    cat(sprintf("%-20s %s\n", pkg, version))
  }
}

cat("\n=== R Session Info ===\n")
cat("R version:", R.version.string, "\n")
cat("Platform:", R.version$platform, "\n")
cat("OS:", Sys.info()["sysname"], Sys.info()["release"], "\n")

cat("\nSetup complete!\n")
