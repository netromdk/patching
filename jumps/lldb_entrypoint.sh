#!/bin/sh
ADDR=`otool -s __TEXT __text $1 | head -n 3 | tail -n 1 | awk '{print $1;}'`
echo "b 0x${ADDR}" > /tmp/.lldbcmds
lldb -s /tmp/.lldbcmds $1
