from plexapi import utils


class TvParentChildMixin:
    """ Mixin for Plex objects that have parent/child relationships (episode/season/show). """

    def _buildRelationalKey(self, key, **key_params):
        """ Returns a key suitable for fetching parent/child TV items

            Parameters:
                key (str): The relational key to be fetched.
                **key_params (dict): Optional query parameters to add to the key, such as
                    'excludeAllLeaves=1' or 'index=0'. Additional XML filters should instead
                    be passed into search functions. See :func:`~plexapi.base.PlexObject.fetchItems`
                    for details.

        """
        if not key:
            return None

        args = {'includeGuids': 1, **key_params}
        params = utils.joinArgs(args).lstrip('?')

        return f"{key}?{params}"
