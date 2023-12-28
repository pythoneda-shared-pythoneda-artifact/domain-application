"""
pythoneda/artifact/application/artifact_app.py

This file defines the ArtifactApp class.

Copyright (C) 2023-today rydnr's pythoneda-shared-pythoneda-artifact-def/domain-application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.shared.artifact import LocalArtifact
from pythoneda.shared.artifact.application import LocalArtifactApp
from pythoneda.artifact.infrastructure import LocalDomainArtifact


class ArtifactApp(LocalArtifactApp):
    """
    Runs the Artifact PythonEDA realm.

    Class name: ArtifactApp

    Responsibilities:
        - Runs the Artifact PythonEDA realm.

    Collaborators:
        - Command-line handlers from pythoneda-shared-pythoneda/domain-artifact-infrastructure
    """

    def __init__(self):
        """
        Creates a new ArtifactApp instance.
        """
        # artifact is automatically generated by pythoneda-shared-pythoneda-artifact-def/domain-application's flake
        try:
            from pythoneda.artifact.application.artifact_banner import ArtifactBanner
            banner = ArtifactBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)

    @classmethod
    def local_artifact_class(cls) -> type[LocalArtifact]:
        """
        Retrieves the subclass of LocalArtifact.
        :return: Such class.
        :rtype: type[LocalArtifact]
        """
        return LocalDomainArtifact


if __name__ == "__main__":
    asyncio.run(ArtifactApp.main("pythoneda.artifact.application.ArtifactApp"))
