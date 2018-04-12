#!/bin/bash -l

# Enable rh-ruby, might be able to remove later
scl enable rh-ruby24 - << \EOF
PUBLIC_WWW=/export/www/wymore
jekyll build --destination $PUBLIC_WWW
exit
EOF
