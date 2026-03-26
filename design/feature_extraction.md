# Feature Extraction Design

## L2_BLUR_001
Blur is calculated using Laplacian variance.

Steps:
1. Convert image to grayscale
2. Apply Laplacian filter
3. Compute variance
4. Compare with threshold

## L2_CONTRAST_001
Contrast is computed using pixel intensity distribution.