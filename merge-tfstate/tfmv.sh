#!/usr/bin/env bash
state_pull() {
    echo ">> state pull"
    cd "$1" || return 1
    terraform init
    terraform state pull >terraform.tfstate
    cd ..
    return 0
}
 
state_mv() {
    echo ">> state mv"
    cd "$2" || return 1
    terraform init
    for i in $(terraform state list); do
        terraform state mv -state-out="../$1/terraform.tfstate" "$i" "$i"
    done
    cd ..
    return 0
}

state_push() {
    echo ">> state push"
    cd "$1" || return 1
    terraform state push terraform.tfstate
    cd ..
    return 0
}

cleanup() {
    echo ">> cleanup"
    cd "$1" || return 1
    rm terraform.tfstate
    rm terraform.tfstate.*
    cd ..
    return 0
}

# Print help text and exit.
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    echo "Usage: tfmv.sh [options]"
    echo
    echo "Examples:"
    echo
    echo "  - ./tfmv.sh stack1-migrate-to stack2-migrate-from"
    echo "  - ./tfmv.sh app data"
    exit 1
fi
echo "> START"
echo ">> TF =  $(terraform version)..."
state_pull "$1"
state_mv "$1" "$2"
state_push "$1"
# cleanup "$1"
echo "> FINISHED"
