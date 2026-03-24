#!/bin/bash
set -e

echo "🤖 Installing Awesome OpenCode Skills..."
INSTALL_DIR="$HOME/.config/opencode/skills"
TMP_DIR=$(mktemp -d)
ZIP_FILE="$TMP_DIR/repo.zip"

echo "📥 Downloading skills pack..."
curl -sL https://github.com/jshsakura/awesome-opencode-skills/archive/refs/heads/main.zip -o "$ZIP_FILE"

echo "📦 Extracting files..."
unzip -q "$ZIP_FILE" -d "$TMP_DIR" > /dev/null

echo "📂 Installing to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
cp -r "$TMP_DIR/awesome-opencode-skills-main/skills/"* "$INSTALL_DIR/"

echo "🧹 Cleaning up..."
rm -rf "$TMP_DIR"

echo "✅ Successfully installed all skills to $INSTALL_DIR"
echo "🚀 You can now use these skills in OpenCode!"
