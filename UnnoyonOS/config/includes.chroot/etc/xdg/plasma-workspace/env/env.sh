## UnnoyonOS XDG configuration
if [ -z "${XDG_CONFIG_DIRS}" ] ; then
    XDG_CONFIG_DIRS=/etc/xdg
    export XDG_CONFIG_DIRS
fi
