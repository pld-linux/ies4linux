#!/bin/sh

##############################################################################
# Blame Andrew Chadwick <andrewc-ies4linux0606@piffle.org>, not Sérgio.
#
# Released under the GNU GPL version 2 (or later, your call).
# See ies4linux's own LICENSE or COPYING file for more information.
##############################################################################

IE=`basename "$0" | awk -F - '{ print $1 }'`
LOCALE=`basename "$0" | sed 's:ie[0-9]*-*::'`
[ "x$LOCALE" == "x" ] && LOCALE="en-US"
MASTERPREFIX="/usr/share/ies4linux/$LOCALE/$IE"
WINEPREFIX="${HOME}/.ies4linux/$IE-$LOCALE"

# If we're not set up, create the user's magic symlink-copy of the master
# installation.

if ! test -d "$WINEPREFIX"; then
    if ! mkdir -p "$WINEPREFIX"; then
        echo "mkdir $WINEPREFIX failed"
        exit 1
    fi
    
    if ! cp -rs $MASTERPREFIX/* "$WINEPREFIX/"; then
        echo "linking failed"
	exit 1
    fi

    # The profile directory will be recreated automatically by wine on the
    # first run, so it's OK to blow away eny existing copy hanging around in
    # unwritable symlink form from the install, and it's OK to just create a
    # blank one.
   
    PROFILES="$WINEPREFIX/drive_c/windows/profiles"
    rm -fr "$PROFILES"
    mkdir -p "$PROFILES"

    # WINE needs to be able to write to the following files, so they can't be
    # symlinks to root-owned ones.
   
    for file in .no_prelaunch_window_flag system.reg userdef.reg user.reg; do
        if test -L "$WINEPREFIX/$file"; then
            rm -f "$WINEPREFIX/$file"
            cp "$MASTERPREFIX/$file" "$WINEPREFIX/$file"
        fi
    done
    chmod -R og-rwx "$WINEPREFIX"
fi

export WINEPREFIX
exec wine "$WINEPREFIX/drive_c/Program Files/Internet Explorer/IEXPLORE.EXE"
echo "Failed to launch WINE: see above for details"
exit 1 

