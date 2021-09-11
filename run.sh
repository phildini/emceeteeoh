#!/bin/bash

SUPERCOLLIDER=${SCEXE:-"/Applications/SuperCollider.app/Contents/MacOS/sclang"}

STARTUP_FILE="./startup.scd"

eval "${SUPERCOLLIDER} ${STARTUP_FILE}"