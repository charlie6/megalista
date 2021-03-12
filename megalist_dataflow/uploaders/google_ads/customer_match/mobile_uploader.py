# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import apache_beam as beam
import logging

from typing import List, Dict, Any

from uploaders.google_ads.customer_match.abstract_uploader import GoogleAdsCustomerMatchAbstractUploaderDoFn
from uploaders import utils as utils
from models.execution import DestinationType, AccountConfig
from models.oauth_credentials import OAuthCredentials


class GoogleAdsCustomerMatchMobileUploaderDoFn(GoogleAdsCustomerMatchAbstractUploaderDoFn):
  def get_list_definition(self, account_config: AccountConfig, destination_metadata: List[str]) -> Dict[str, Any]:
    list_name = destination_metadata[0]    
    app_id = account_config.app_id
    
    #overwrite app_id from default to custom
    if len(destination_metadata) >=4 and len(destination_metadata[3]) > 0:
        app_id = destination_metadata[3]

    return {
      'operand': {
        'xsi_type': 'CrmBasedUserList',
        'name': list_name,
        'description': list_name,
        # CRM-based user list_name can use a membershipLifeSpan of 10000 to indicate
        # unlimited; otherwise normal values apply.
        'membershipLifeSpan': 10000,
        'appId': app_id,
        'uploadKeyType': 'MOBILE_ADVERTISING_ID'
      }
    }

  def get_row_keys(self) -> List[str]:
    return ['mobileId']

  def get_action_type(self) -> DestinationType:
    return DestinationType.ADS_CUSTOMER_MATCH_MOBILE_DEVICE_ID_UPLOAD
