#!/usr/bin/env python3
"""
Standalone test to verify watchlist uses DISCOVER endpoint.
"""

import unittest
from unittest.mock import MagicMock, patch
from plexapi.myplex import MyPlexAccount


class TestWatchlistEndpoint(unittest.TestCase):
    def test_watchlist_uses_discover_endpoint(self):
        """Test that watchlist method uses DISCOVER endpoint instead of METADATA."""
        # Create a MyPlexAccount instance
        account = MyPlexAccount.__new__(MyPlexAccount)
        account._token = "test_token"
        account._session = MagicMock()
        account._timeout = 30
        
        # Mock the fetchItems and _toOnlineMetadata methods
        with patch.object(MyPlexAccount, 'fetchItems', return_value=[]) as mock_fetchItems, \
             patch.object(MyPlexAccount, '_toOnlineMetadata', return_value=[]) as mock_toOnlineMetadata:
            
            # Call the watchlist method
            result = MyPlexAccount.watchlist(account, filter='all')
            
            # Verify that fetchItems was called
            self.assertTrue(mock_fetchItems.called)
            
            # Get the URL that was passed to fetchItems
            url_arg = mock_fetchItems.call_args[0][0]
            
            # Verify that the URL starts with DISCOVER endpoint
            self.assertTrue(url_arg.startswith(MyPlexAccount.DISCOVER), 
                          f"Expected URL to start with {MyPlexAccount.DISCOVER}, got {url_arg}")
            
            # Verify that METADATA endpoint is not used
            self.assertNotIn(MyPlexAccount.METADATA, url_arg, 
                           f"URL should not contain METADATA endpoint: {url_arg}")
            
            # Verify the exact expected URL pattern
            self.assertTrue('/library/sections/watchlist/all' in url_arg,
                          f"URL should contain watchlist path: {url_arg}")

if __name__ == '__main__':
    unittest.main()
