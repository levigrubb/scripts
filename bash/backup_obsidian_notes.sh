#!/bin/bash

cd "~/Documents/Obsidian Vault/"
git add .
git commit -m "standard backup commit @$(date)"
git push
