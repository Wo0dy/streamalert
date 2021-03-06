"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import logging
import logging.handlers


def set_logger_levels(debug=False):
    """Set all of the logger levels

    Args:
        debug (bool): True to enable debug logging, False otherwise
    """
    for name, logger in logging.Logger.manager.loggerDict.iteritems():
        if isinstance(logger, logging.PlaceHolder):
            continue

        if debug and name.startswith('stream_alert'):
            logger.setLevel(logging.DEBUG if debug else logging.INFO)
        elif name.startswith(__package__):
            logger.setLevel(logging.INFO)
        else:
            logger.disabled = True  # disable this logger if it's not one of ours
