# Copyright 2014-2015 Canonical Limited.
#
# This file is part of charm-helpers.
#
# charm-helpers is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3 as
# published by the Free Software Foundation.
#
# charm-helpers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with charm-helpers.  If not, see <http://www.gnu.org/licenses/>.

from .bus import set_state  # noqa
from .bus import remove_state  # noqa
from .relations import scopes  # noqa
from .relations import RelationBase  # noqa
from .decorators import hook  # noqa
from .decorators import when  # noqa
from .decorators import when_not  # noqa
from .decorators import when_file_changed  # noqa
from .decorators import not_until  # noqa

from . import bus
from charmhelpers.core import unitdata


def main(relation_name=None):
    """
    This is the main entry point for the reactive framework.  It calls
    :func:`~bus.discover` to find and load all reactive handlers (e.g.,
    :func:`@when <decorators.when>` decorated blocks), and then
    :func:`~bus.dispatch` to trigger hook and state handlers until the
    state settles out.  Finally,
    :meth:`unitdata.kv().flush <charmhelpers.core.unitdata.Storage.flush>`
    is called to persist the state.

    :param str relation_name: Optional name of the relation which is being handled.
    """
    bus.discover()
    bus.dispatch()
    if unitdata._KV:
        unitdata._KV.flush()
