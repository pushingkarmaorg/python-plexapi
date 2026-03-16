from plexapi import utils


class TvParentChildMixin:
    """ Mixin for Plex objects that have parent/child relationships (episode/season/show). """

    def _buildRelationKey(self, key, **kwargs):
        """ Returns a key suitable for fetching parent/child TV items

            Parameters:
                key (str): The relational key being fetched, such as '/children' (may be
                    empty).
                **kwargs (dict): Custom XML attribute filters to apply to add to the
                    query. See :func:`~plexapi.base.PlexObject.fetchItems` for more
                    details on how this is used.

        """
        if not key:
            return None

        args = {'includeGuids': 1, **kwargs}
        params = utils.joinArgs(args).lstrip('?')

        return f"{key}?{params}"
