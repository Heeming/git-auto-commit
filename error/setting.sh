#!/bin/bash
git config --global credential.helper store
git config --global credential.helpter cache

git --no-pager

git checkout -b auto-commit
