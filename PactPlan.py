import logging

import uvicorn

from pactplan import PP_APP

app = PP_APP

if __name__ == "__main__":
    logging.warning("Your server is running via development mode. "
                    "PLEASE DO NOT RUN AT PRODUCTION!")
    uvicorn.run(
        "PactPlan:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
