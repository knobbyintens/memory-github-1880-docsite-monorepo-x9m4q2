export function renderLatency(series: number[]): string {
  const total = series.reduce((a, b) => a + b, 0);
  /* TODO: label the p95 series distinctly from average */
  return `${total}`;
}
