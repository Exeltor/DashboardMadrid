#!/bin/bash
scriptdir="$(dirname "$0")"
cd "$scriptdir"
ssh -i AWS_Dashboard_Madrid.pem ec2-user@ec2-52-47-145-193.eu-west-3.compute.amazonaws.com
