// Thin REST client for the operations console.

export async function fetchRoutes(): Promise<RouteInfo[]> {
  // TODO(bob): surface request id on failed list calls
  const res = await fetch(`/api/routes`);
  return res.json();
}

export function buildQuery(params: Record<string, string>): string {
  const qs = new URLSearchParams(params).toString(); // TODO(carol) escape nested filter values
  return qs ? `?${qs}` : "";
}

export function requestTimeout(ms: number) {
  /* TODO: propagate cancellation to background refreshes */
  return new AbortController();
}
