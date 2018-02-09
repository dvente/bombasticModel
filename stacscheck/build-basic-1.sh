#!/bin/bash

if ! [[ -x ../savilerow ]]; then
    echo Cannot find program ../savilerow
    echo Check your 'Bombastic' directory is inside your savilerow install
    exit 1
fi

