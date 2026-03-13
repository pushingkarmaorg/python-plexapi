from plexapi import utils

class TvParentChildMixin:
    """ Mixin for Plex objects that have parent/child relationships (episode/season/show). """

    def _buildRelationKey(self, key, **kwargs):
        """ Returns a key suitable for fetching parent/child TV items """
        args = {}

        args['includeGuids'] = int(bool(kwargs.pop('includeGuids', True)))
        for name, value in list(kwargs.items()):
            args[name] = value

        params = utils.joinArgs(args).lstrip('?')

        return f"{key}?{params}"