// SPDX-License-Identifier: Apache-2.0
// Notification helpers for the operations console

export function notify(channel: string, text: string) {
  // TODO(erin): dedupe alerts by fingerprint within one minute
  send(channel, text);
}

export function banner(message: string) {
  const el = document.getElementById("banner");
  if (el) el.textContent = message;
}

export function flushBanners() {
  // TODO(bob): notification batching: combine repeated banners
  queue.flush();
}
