#!/bin/bash
export $(grep -v '^#' ../API.env | xargs)
