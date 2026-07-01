There is an Apache-style access log at `/app/access.log`. Each non-empty line is one
request and begins with the client IP address, followed by the usual common-log fields,
including a quoted request line such as `"GET /index.html HTTP/1.1"`.

Parse the log and write a summary report to `/app/report.json`. The report must be a
single JSON object with exactly these three keys:

- `total_requests`: integer - the number of non-empty request lines in the log.
- `unique_ips`: integer - the number of distinct client IP addresses (the first
  whitespace-separated field on each line).
- `top_path`: string - the request path (the second token inside the quoted request,
  e.g. `/index.html`) that appears most often across all requests.

Success criteria:

1. A file exists at `/app/report.json` and its contents parse as a single JSON object.
2. `total_requests` is an integer equal to the number of non-empty request lines.
3. `unique_ips` is an integer equal to the number of distinct client IP addresses.
4. `top_path` is a string equal to the most frequently requested path.
