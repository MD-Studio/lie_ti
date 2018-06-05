# -*- coding: utf-8 -*-

"""
file: wamp_services.py

WAMP service methods the module exposes.
"""
from mdstudio.api.endpoint import endpoint
from mdstudio.deferred.chainable import chainable
from mdstudio.component.session import ComponentSession
from mdstudio.deferred.return_value import return_value


class Gromacs_ti_wamp_api(ComponentSession):
    """
    Gromacs based Thermodynamic Integration (TI) WAMP methods.
    """
    def authorize_request(self, uri, claims):
        return True

    @endpoint('gromacs_ti', 'gromacs_ti_request', 'gromacs_ti_response')
    @chainable
    def run_gromacs_ti(self, request, claims):
        """
        """
        task_id = self.component_config.session.session_id
        request.update({"task_id": task_id})
        self.log.info("starting lie_ti task_id:{}".format(task_id))

        output = {'answer': 42}

        status = 'failed' if output is None else 'completed'

        return_value(
            {'status': status, 'output': output})
