export function notify(channel: string, text: string) {
  // TODO(erin): dedupe alerts by fingerprint within one minute
  send(channel, text);
}

export function banner(message: string) {
  const el = document.getElementById("banner"); // TODO(carol) restore keyboard focus after banner dismissal
  if (el) el.textContent = message;
}
