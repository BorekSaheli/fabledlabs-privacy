"""Generates the FabledLabs privacy policy site. Add an entry to APPS and rerun: uv run build.py"""
import html
from pathlib import Path

UPDATED = "September 29, 2026"
OUT = Path(__file__).parent / "docs"

ADS_SECTION = """
<h2>Advertising (Google AdMob)</h2>
<p>The free version shows ads served by Google AdMob. To show and measure ads, and to prevent fraud, the
Google Mobile Ads SDK may collect and process data such as your device's advertising ID, IP address, coarse
location derived from the IP address, device model and OS version, and interactions with ads. This data is
collected by Google, not by us, and is handled under
<a href="https://policies.google.com/privacy">Google's Privacy Policy</a>
(see also <a href="https://policies.google.com/technologies/partner-sites">how Google uses data from apps that use its services</a>).</p>
<p>If you are in the European Economic Area, the UK or Switzerland, the app asks for your consent before
personalized ads are shown, using Google's consent tool. You can change your choice at any time from the
app's Settings screen ("Ad privacy choices"). You can also reset or delete your advertising ID in your
Android device settings. Buying "Remove ads" turns off banner and full-screen ads.</p>
"""

BILLING_SECTION = """
<h2>In-app purchases</h2>
<p>Purchases are processed by Google Play. We never see or store your payment details. The app only
receives a confirmation of which items you own so it can unlock them.</p>
"""

APPS = [
    {
        "slug": "logic-trio",
        "name": "Logic Trio: Daily Puzzles",
        "package": "com.fabledlabs.logictrio",
        "local": "your puzzle progress, streaks, statistics, hint balance and settings",
        "ads": True,
        "billing": True,
        "extra": "",
    },
    {
        "slug": "study-scanner",
        "name": "Study Scanner: PDF & Notes",
        "package": "com.fabledlabs.studyscanner",
        "local": "your scanned page images, the text recognized from them, document titles, courses and settings",
        "ads": True,
        "billing": True,
        "extra": """
<h2>Camera, scanning and text recognition</h2>
<p>Scanning uses Google's ML Kit Document Scanner, which runs inside Google Play services on your device. The app itself
does not request camera permission. Text recognition uses Google's on-device ML Kit model: your images are
processed on your phone and are not sent to us or to Google for recognition. Google Play services may collect
basic diagnostic and usage information about these ML Kit features, as described in
<a href="https://developers.google.com/ml-kit/terms">Google's ML Kit terms</a>.</p>
<p>When you share or export a PDF, it goes only where you choose to send it through the Android share sheet.</p>
""",
    },
    {
        "slug": "fix-and-flip",
        "name": "Fix & Flip: Cozy Repair Shop",
        "package": "com.fabledlabs.repairshop",
        "local": "your game progress (coins, items, upgrades), purchases and settings",
        "ads": True,
        "billing": True,
        "extra": "",
    },
    {
        "slug": "repbook",
        "name": "RepBook: Offline Gym Log",
        "package": "com.fabledlabs.repbook",
        "local": "your workouts, sets, routines, custom exercises and settings",
        "ads": False,
        "billing": True,
        "extra": """
<h2>No ads, no tracking</h2>
<p>RepBook contains no advertising or analytics SDKs and does not access the internet except to process an optional
purchase through Google Play. Backups and CSV exports are created only when you choose to, and are shared only where you send them.</p>
""",
    },
    {
        "slug": "pawpath",
        "name": "PawPath: Dog Training Program",
        "package": "com.fabledlabs.pawpath",
        "local": "your dog's name and age group, your logged training sessions, streaks and settings",
        "ads": False,
        "billing": True,
        "extra": """
<h2>No ads, no tracking</h2>
<p>PawPath contains no advertising or analytics SDKs. All lessons are bundled in the app, and the app does not access
the internet except to process an optional purchase through Google Play.</p>
""",
    },
    {
        "slug": "pop-clinic",
        "name": "Pop Clinic: Satisfying Pops",
        "package": "com.fabledlabs.popclinic",
        "local": "your level progress, stars, unlocked instruments and themes, purchases and settings",
        "ads": True,
        "billing": True,
        "extra": """
<h2>Vibration</h2>
<p>The app uses your phone's vibration motor for haptic feedback. You can turn it off in Settings.</p>
""",
    },
    {
        "slug": "neon-flip",
        "name": "Neon Flip: Pinball Roguelite",
        "package": "com.fabledlabs.neonflip",
        "local": "your best score, coins, upgrades, purchases and settings",
        "ads": True,
        "billing": True,
        "extra": "",
    },
]


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:760px;margin:0 auto;padding:32px 20px 64px;line-height:1.6;color:#2b2a33;background:#fbfaf7}}
h1{{font-size:1.8rem;margin-bottom:.2rem}} h2{{font-size:1.15rem;margin-top:2rem}}
.muted{{color:#777}} a{{color:#3a6fd8}} li{{margin:.3rem 0}}
</style></head><body>
{body}
<p class="muted" style="margin-top:3rem">&copy; 2026 FabledLabs</p>
</body></html>
"""


def app_page(a: dict) -> str:
    parts = [f"<h1>Privacy Policy &mdash; {html.escape(a['name'])}</h1>",
             f"<p class='muted'>Developer: FabledLabs &middot; App ID: {a['package']} &middot; Last updated: {UPDATED}</p>",
             "<h2>Summary</h2>",
             "<ul><li>No account or sign-up is needed.</li>"
             "<li>We (FabledLabs) do not run servers and do not collect, receive or sell your personal data.</li>"
             f"<li>The app stores {a['local']} only on your device.</li>"
             + ("<li>Ads are provided by Google AdMob, which may collect device data as described below.</li>" if a["ads"] else "")
             + "</ul>",
             "<h2>Data stored on your device</h2>",
             f"<p>The app keeps {a['local']} in its private storage on your device. This data never leaves your device "
             "through us. It is removed when you uninstall the app or clear its data. It may be included in your own "
             "Android device backup if you have backups enabled, which is governed by Google's terms.</p>"]
    if a["extra"]:
        parts.append(a["extra"])
    if a["ads"]:
        parts.append(ADS_SECTION)
    if a["billing"]:
        parts.append(BILLING_SECTION)
    parts.append("""
<h2>Children</h2>
<p>The app is not directed at children under 13, and we do not knowingly collect personal information from children.</p>
<h2>Security</h2>
<p>Data exchanged with Google's ad and billing services is encrypted in transit (HTTPS).</p>
<h2>Changes</h2>
<p>We may update this policy. The "last updated" date above shows the latest version.</p>
<h2>Contact</h2>
<p>Questions or requests: use the developer email address shown on the app's Google Play store page, or open an issue at
<a href="https://github.com/BorekSaheli/fabledlabs-privacy/issues">github.com/BorekSaheli/fabledlabs-privacy</a>.</p>
""")
    return page(f"Privacy Policy - {a['name']}", "\n".join(parts))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / ".nojekyll").write_text("")
    items = []
    for a in APPS:
        (OUT / f"{a['slug']}.html").write_text(app_page(a), encoding="utf-8")
        items.append(f"<li><a href='{a['slug']}.html'>{html.escape(a['name'])}</a></li>")
    (OUT / "index.html").write_text(page("FabledLabs - Privacy", "<h1>FabledLabs</h1><p>Privacy policies for our Android apps:</p><ul>"
                                         + "".join(items) + "</ul>"), encoding="utf-8")


if __name__ == "__main__":
    main()
