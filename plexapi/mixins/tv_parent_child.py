from plexapi import utils


class TvParentChildMixin:
    """ Mixin for Plex objects that have parent/child relationships (episode/season/show). """

    def _buildRelationalKey(self, key, **kwargs):
        """ Returns a key suitable for fetching parent/child TV items

            Parameters:
                key (str): The relational key to be fetched.
                **kwargs (dict): Optional relational selection parameters to apply to the
                    key, for example 'excludeAllLeaves=1'. Additional options (such as XML
                    filters) should be passed into search functions. See :func:`~plexapi.base.PlexObject.fetchItems`
                    for details.

        """
        if not key:
            return None

        args = {'includeGuids': 1, **kwargs}
        params = utils.joinArgs(args).lstrip('?')

        return f"{key}?{params}"
