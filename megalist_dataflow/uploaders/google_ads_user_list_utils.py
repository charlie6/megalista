# Copyright 2020 Google LLC
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


def get_user_list_service(oauth_credentials, developer_token, customer_id):
  from googleads import adwords
  from googleads import oauth2
  oauth2_client = oauth2.GoogleRefreshTokenClient(
    oauth_credentials.get_client_id(), oauth_credentials.get_client_secret(), oauth_credentials.get_refresh_token())
  client = adwords.AdWordsClient(developer_token, oauth2_client, 'MegaList Dataflow', client_customer_id=customer_id)
  return client.GetService('AdwordsUserListService', 'v201809')


def assert_elements_have_same_execution(elements):
  last_execution = elements[0]['execution']
  for element in elements:
    current_execution = element['execution']
    if current_execution != last_execution:
      raise ValueError(
        'At least two Execution in a single call ({}) and ({})'.format(str(current_execution), str(last_execution)))
    last_execution = current_execution
