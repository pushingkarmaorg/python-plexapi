#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plex-RefreshToken is a simple method to refresh a Plex account token by pinging Plex.tv.
"""
import argparse

import plexapi
from plexapi.myplex import MyPlexAccount


def refresh_token(token):
    """Refresh the Plex authentication token."""
    account = MyPlexAccount(token=token)
    if account.ping():
        print("Plex.tv authentication token refreshed successfully.")
    else:
        print("Failed to refresh Plex.tv authentication token.")
        exit(1)


if __name__ == "__main__":  # noqa: C901
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--token",
        help="Plex.tv authentication token",
        default=plexapi.CONFIG.get("auth.server_token"),
    )

    args = parser.parse_args()
    if not args.token:
        print("No Plex.tv authentication token provided.")
        exit(1)

    refresh_token(args.token)
