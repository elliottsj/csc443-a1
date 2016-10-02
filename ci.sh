#!/usr/bin/env bash
# Unofficial bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

# Show commands before executing
set -o xtrace

# Add CDF to known_hosts
cat << EOF >> ~/.ssh/known_hosts
wolf.teach.cs.toronto.edu,128.100.31.200 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAvphXfsPWt/LnAf5JF/xJVsP72LqjDBUPdr5u7jS6R+C0FuI5dSkz92Mlnpvcyhn/iv3TMD+va77P1rzMbiRoJBIVDpGgwQGQjWatvAVaOZ2uXawoK5DJES8ld1oMJ4tALo5REmoupLU1pxygxrfSuIoKWAsYbkin3softNyVNDs=
EOF

# Decode SSH key
echo $CDF_DEPLOY_KEY | base64 --decode > ./id_ed25519
chmod 600 ./id_ed25519

# Run tests on CDF
ssh -i ./id_ed25519 ellio128@wolf.teach.cs.toronto.edu << EOF
    cd csc443
    rm -rf csc443-a1
    git clone --branch $CIRCLE_BRANCH git@github.com:elliottsj/csc443-a1.git csc443-a1
    cd csc443-a1
    ./cdf_test.sh
EOF
