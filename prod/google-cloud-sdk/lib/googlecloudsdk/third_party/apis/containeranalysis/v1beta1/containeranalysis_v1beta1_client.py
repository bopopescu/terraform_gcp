"""Generated client library for containeranalysis version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.containeranalysis.v1beta1 import containeranalysis_v1beta1_messages as messages


class ContaineranalysisV1beta1(base_api.BaseApiClient):
  """Generated client library for service containeranalysis version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://containeranalysis.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'containeranalysis'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ContaineranalysisV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new containeranalysis handle."""
    url = url or self.BASE_URL
    super(ContaineranalysisV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_notes_occurrences = self.ProjectsNotesOccurrencesService(self)
    self.projects_notes = self.ProjectsNotesService(self)
    self.projects_occurrences = self.ProjectsOccurrencesService(self)
    self.projects_scanConfigs = self.ProjectsScanConfigsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsNotesOccurrencesService(base_api.BaseApiService):
    """Service class for the projects_notes_occurrences resource."""

    _NAME = u'projects_notes_occurrences'

    def __init__(self, client):
      super(ContaineranalysisV1beta1.ProjectsNotesOccurrencesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists occurrences referencing the specified note. Provider projects can use.
this method to get all occurrences across consumer projects referencing the
specified note.

      Args:
        request: (ContaineranalysisProjectsNotesOccurrencesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNoteOccurrencesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}/occurrences',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.notes.occurrences.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+name}/occurrences',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsNotesOccurrencesListRequest',
        response_type_name=u'ListNoteOccurrencesResponse',
        supports_download=False,
    )

  class ProjectsNotesService(base_api.BaseApiService):
    """Service class for the projects_notes resource."""

    _NAME = u'projects_notes'

    def __init__(self, client):
      super(ContaineranalysisV1beta1.ProjectsNotesService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchCreate(self, request, global_params=None):
      r"""Creates new notes in batch.

      Args:
        request: (ContaineranalysisProjectsNotesBatchCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchCreateNotesResponse) The response message.
      """
      config = self.GetMethodConfig('BatchCreate')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchCreate.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes:batchCreate',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.notes.batchCreate',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}/notes:batchCreate',
        request_field=u'batchCreateNotesRequest',
        request_type_name=u'ContaineranalysisProjectsNotesBatchCreateRequest',
        response_type_name=u'BatchCreateNotesResponse',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates a new note.

      Args:
        request: (ContaineranalysisProjectsNotesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Note) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.notes.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'noteId'],
        relative_path=u'v1beta1/{+parent}/notes',
        request_field=u'note',
        request_type_name=u'ContaineranalysisProjectsNotesCreateRequest',
        response_type_name=u'Note',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified note.

      Args:
        request: (ContaineranalysisProjectsNotesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}',
        http_method=u'DELETE',
        method_id=u'containeranalysis.projects.notes.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsNotesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the specified note.

      Args:
        request: (ContaineranalysisProjectsNotesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Note) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.notes.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsNotesGetRequest',
        response_type_name=u'Note',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a note or an occurrence resource.
Requires `containeranalysis.notes.setIamPolicy` or
`containeranalysis.occurrences.setIamPolicy` permission if the resource is
a note or occurrence, respectively.

The resource takes the format `projects/[PROJECT_ID]/notes/[NOTE_ID]` for
notes and `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]` for
occurrences.

      Args:
        request: (ContaineranalysisProjectsNotesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.notes.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'ContaineranalysisProjectsNotesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists notes for the specified project.

      Args:
        request: (ContaineranalysisProjectsNotesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNotesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.notes.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/notes',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsNotesListRequest',
        response_type_name=u'ListNotesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the specified note.

      Args:
        request: (ContaineranalysisProjectsNotesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Note) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}',
        http_method=u'PATCH',
        method_id=u'containeranalysis.projects.notes.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1beta1/{+name}',
        request_field=u'note',
        request_type_name=u'ContaineranalysisProjectsNotesPatchRequest',
        response_type_name=u'Note',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified note or occurrence.
Requires `containeranalysis.notes.setIamPolicy` or
`containeranalysis.occurrences.setIamPolicy` permission if the resource is
a note or an occurrence, respectively.

The resource takes the format `projects/[PROJECT_ID]/notes/[NOTE_ID]` for
notes and `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]` for
occurrences.

      Args:
        request: (ContaineranalysisProjectsNotesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.notes.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'ContaineranalysisProjectsNotesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns the permissions that a caller has on the specified note or.
occurrence. Requires list permission on the project (for example,
`containeranalysis.notes.list`).

The resource takes the format `projects/[PROJECT_ID]/notes/[NOTE_ID]` for
notes and `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]` for
occurrences.

      Args:
        request: (ContaineranalysisProjectsNotesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/notes/{notesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.notes.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'ContaineranalysisProjectsNotesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsOccurrencesService(base_api.BaseApiService):
    """Service class for the projects_occurrences resource."""

    _NAME = u'projects_occurrences'

    def __init__(self, client):
      super(ContaineranalysisV1beta1.ProjectsOccurrencesService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchCreate(self, request, global_params=None):
      r"""Creates new occurrences in batch.

      Args:
        request: (ContaineranalysisProjectsOccurrencesBatchCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchCreateOccurrencesResponse) The response message.
      """
      config = self.GetMethodConfig('BatchCreate')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchCreate.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences:batchCreate',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.occurrences.batchCreate',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}/occurrences:batchCreate',
        request_field=u'batchCreateOccurrencesRequest',
        request_type_name=u'ContaineranalysisProjectsOccurrencesBatchCreateRequest',
        response_type_name=u'BatchCreateOccurrencesResponse',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates a new occurrence.

      Args:
        request: (ContaineranalysisProjectsOccurrencesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Occurrence) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.occurrences.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}/occurrences',
        request_field=u'occurrence',
        request_type_name=u'ContaineranalysisProjectsOccurrencesCreateRequest',
        response_type_name=u'Occurrence',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified occurrence. For example, use this method to delete an.
occurrence when the occurrence is no longer applicable for the given
resource.

      Args:
        request: (ContaineranalysisProjectsOccurrencesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}',
        http_method=u'DELETE',
        method_id=u'containeranalysis.projects.occurrences.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsOccurrencesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the specified occurrence.

      Args:
        request: (ContaineranalysisProjectsOccurrencesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Occurrence) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.occurrences.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsOccurrencesGetRequest',
        response_type_name=u'Occurrence',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a note or an occurrence resource.
Requires `containeranalysis.notes.setIamPolicy` or
`containeranalysis.occurrences.setIamPolicy` permission if the resource is
a note or occurrence, respectively.

The resource takes the format `projects/[PROJECT_ID]/notes/[NOTE_ID]` for
notes and `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]` for
occurrences.

      Args:
        request: (ContaineranalysisProjectsOccurrencesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.occurrences.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'ContaineranalysisProjectsOccurrencesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def GetNotes(self, request, global_params=None):
      r"""Gets the note attached to the specified occurrence. Consumer projects can.
use this method to get a note that belongs to a provider project.

      Args:
        request: (ContaineranalysisProjectsOccurrencesGetNotesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Note) The response message.
      """
      config = self.GetMethodConfig('GetNotes')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetNotes.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}/notes',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.occurrences.getNotes',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}/notes',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsOccurrencesGetNotesRequest',
        response_type_name=u'Note',
        supports_download=False,
    )

    def GetVulnerabilitySummary(self, request, global_params=None):
      r"""Gets a summary of the number and severity of occurrences.

      Args:
        request: (ContaineranalysisProjectsOccurrencesGetVulnerabilitySummaryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (VulnerabilityOccurrencesSummary) The response message.
      """
      config = self.GetMethodConfig('GetVulnerabilitySummary')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetVulnerabilitySummary.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences:vulnerabilitySummary',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.occurrences.getVulnerabilitySummary',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter'],
        relative_path=u'v1beta1/{+parent}/occurrences:vulnerabilitySummary',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsOccurrencesGetVulnerabilitySummaryRequest',
        response_type_name=u'VulnerabilityOccurrencesSummary',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists occurrences for the specified project.

      Args:
        request: (ContaineranalysisProjectsOccurrencesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOccurrencesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.occurrences.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/occurrences',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsOccurrencesListRequest',
        response_type_name=u'ListOccurrencesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the specified occurrence.

      Args:
        request: (ContaineranalysisProjectsOccurrencesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Occurrence) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}',
        http_method=u'PATCH',
        method_id=u'containeranalysis.projects.occurrences.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1beta1/{+name}',
        request_field=u'occurrence',
        request_type_name=u'ContaineranalysisProjectsOccurrencesPatchRequest',
        response_type_name=u'Occurrence',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified note or occurrence.
Requires `containeranalysis.notes.setIamPolicy` or
`containeranalysis.occurrences.setIamPolicy` permission if the resource is
a note or an occurrence, respectively.

The resource takes the format `projects/[PROJECT_ID]/notes/[NOTE_ID]` for
notes and `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]` for
occurrences.

      Args:
        request: (ContaineranalysisProjectsOccurrencesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.occurrences.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'ContaineranalysisProjectsOccurrencesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns the permissions that a caller has on the specified note or.
occurrence. Requires list permission on the project (for example,
`containeranalysis.notes.list`).

The resource takes the format `projects/[PROJECT_ID]/notes/[NOTE_ID]` for
notes and `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]` for
occurrences.

      Args:
        request: (ContaineranalysisProjectsOccurrencesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/occurrences/{occurrencesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'containeranalysis.projects.occurrences.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'ContaineranalysisProjectsOccurrencesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsScanConfigsService(base_api.BaseApiService):
    """Service class for the projects_scanConfigs resource."""

    _NAME = u'projects_scanConfigs'

    def __init__(self, client):
      super(ContaineranalysisV1beta1.ProjectsScanConfigsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the specified scan configuration.

      Args:
        request: (ContaineranalysisProjectsScanConfigsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ScanConfig) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/scanConfigs/{scanConfigsId}',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.scanConfigs.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsScanConfigsGetRequest',
        response_type_name=u'ScanConfig',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists scan configurations for the specified project.

      Args:
        request: (ContaineranalysisProjectsScanConfigsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListScanConfigsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/scanConfigs',
        http_method=u'GET',
        method_id=u'containeranalysis.projects.scanConfigs.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/scanConfigs',
        request_field='',
        request_type_name=u'ContaineranalysisProjectsScanConfigsListRequest',
        response_type_name=u'ListScanConfigsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates the specified scan configuration.

      Args:
        request: (ScanConfig) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ScanConfig) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/scanConfigs/{scanConfigsId}',
        http_method=u'PUT',
        method_id=u'containeranalysis.projects.scanConfigs.update',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='<request>',
        request_type_name=u'ScanConfig',
        response_type_name=u'ScanConfig',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(ContaineranalysisV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
