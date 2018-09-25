# -*- coding: utf-8 -*-
#
# Copyright (c) 2018, Marcelo Jorge Vieira <metal@alucinados.com>
#
#  This program is free software: you can redistribute it and/or modify it
#  under the terms of the GNU Affero General Public License as published by the
#  Free Software Foundation, either version 3 of the License, or (at your
#  option) any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
#  for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.

from tornado.template import Loader

from politicos_api.cache import cache
from politicos_api.handlers.base import BaseHandler


class RoutesHandler(BaseHandler):

    @cache(5)
    async def get(self):
        handlers = []
        for x in self.application.handlers_api:
            # FIXME
            url = x.reverse().replace('?', '')
            handlers.append({'name': x.name, 'url': url})
        if handlers:
            handlers = sorted(handlers, key=lambda k: k['name'])
        loader = Loader('politicos_api/templates')
        content = loader.load('routes.html').generate(handlers=handlers)
        await self.write(content)