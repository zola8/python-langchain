import os

from dotenv import load_dotenv
from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider
from fastmcp.server.dependencies import get_access_token
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BASE_URL = os.getenv("BASE_URL")

# The GitHubProvider handles GitHub's token format and validation
auth_provider = GitHubProvider(
    client_id=CLIENT_ID,  # Your GitHub OAuth App Client ID
    client_secret=CLIENT_SECRET,  # Your GitHub OAuth App Client Secret
    base_url=BASE_URL,  # Must match your OAuth App configuration
    # redirect_path="/auth/callback"   # Default value, customize if needed
)

mcp = FastMCP(name="GitHub Secured App", auth=auth_provider)


@mcp.tool(description="Greeting a user.")
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated GitHub user."""

    token = get_access_token()
    # The GitHubProvider stores user data in token claims
    return {
        "github_user": token.claims.get("login"),
        "name": token.claims.get("name"),
        "email": token.claims.get("email")
    }


# https://gofastmcp.com/integrations/github

if __name__ == "__main__":
    mcp.run(
        transport="http",
        # middleware=[
        #     Middleware(
        #         CORSMiddleware,
        #         allow_origins=["*"],
        #         allow_credentials=True,
        #         allow_methods=["*"],
        #         allow_headers=["*"],
        #     )
        # ]

    )
