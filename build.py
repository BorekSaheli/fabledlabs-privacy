"""Generates the FabledLabs privacy policy site. Add an entry to APPS and rerun: uv run build.py"""
import html
from pathlib import Path

UPDATED = "September 29, 2026"
OUT = Path(__file__).parent / "docs"

ADS_SECTION = """
<h2>Advertising (Google AdMob)</h2>
<p>The free version shows ads served by Google AdMob. To show and measure ads, and to prevent fraud, the
Google Mobile Ads SDK may collect and process data such as your device's advertising ID, IP address, coarse
location derived from the IP address, device model and OS version, and interactions with ads{ads_more}. This data is
collected by Google, not by us, and is handled under
<a href="https://policies.google.com/privacy">Google's Privacy Policy</a>
(see also <a href="https://policies.google.com/technologies/partner-sites">how Google uses data from apps that use its services</a>).</p>
<p>If you are in the European Economic Area, the UK or Switzerland, the app asks for your consent before
personalized ads are shown, using Google's consent tool. You can change your choice at any time from the
app's Settings screen ("Ad privacy choices"). You can also reset or delete your advertising ID in your
Android device settings. {remove_ads}</p>
"""
# Per app (optional keys): "updated" (its own last-updated date), "ads_more" (more Ads SDK data, after "interactions
# with ads"), "remove_ads" (what buying Remove ads does), "children" (the Children paragraph).
REMOVE_ADS = 'Buying "Remove ads" turns off banner and full-screen ads.'
CHILDREN = "The app is not directed at children under 13, and we do not knowingly collect personal information from children."

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
        "local": ("your game progress (patients treated, Career progress, coins, instruments, the looks you own and "
                  "wear, the daily bonus), the items you bought, your settings and the age you entered"),
        "ads": True,
        "billing": True,
        "updated": "November 10, 2026",
        "analytics": True,
        "ads_more": ", and diagnostic and crash information about the ads SDK",
        "remove_ads": ("The app shows a full-screen ad after some results. Any purchase, such as \"Remove ads\", turns "
                       "those full-screen ads off. Short videos that pay in-game coins stay available, and you only "
                       "see one when you choose to watch it. The app shows no banner ads."),
        "children": ("The app is not directed at children under 13, and we do not knowingly collect personal "
                     "information from children. Players under 16 are treated as below the age of digital consent: "
                     "their ad requests are marked as child-directed and under the age of consent, so Google serves "
                     "them non-personalized ads only."),
        "extra": """
<h2>Age question</h2>
<p>When you first open the app, it asks how old you are. The answer stays on your device, in its own file, and is never
sent to us. The app uses it to decide whether analytics may be used (see "Analytics" below) and to configure
Google's ads and consent tools for players under 16 (see "Children" below). You are asked again if you start over as a new player.</p>
<h2>Analytics</h2>
<p>FabledLabs uses Google Analytics for Firebase to learn how people play: the customers they treat and how each spot went (for example how many tries it took, how long, how hard the in-game squeeze was and how close the fingers were to the spot, as summary numbers, never the finger movements themselves), the screens they visit, their in-game settings, what they look at and buy in the shop, coins earned and spent, how they respond to ads (for example a video offered, watched or skipped), and how the game runs on their phone (loading times, slow frames, the graphics chip's name, and errors such as a save that could not be written). Events include screens, tools, items, timings, ad outcomes and purchase outcomes. Google Analytics links these events with a random app-instance identifier stored on your device and processes device and app information and an approximate location (country or region). It does not receive your name, an account, the age you entered, your advertising ID or purchase tokens. FabledLabs links Google Analytics with its Google AdMob and Google Play accounts, so that ad performance, ad earnings and purchases can be seen next to how the game is played; through these links Google Analytics and AdMob share reports with each other. The app tells Google Analytics that its data may not be used for ads: no advertising storage, no ad user data and no ad personalization, so it is not used to choose or personalize the ads you see.</p>
<p>What happens depends on the country of your Google Play account. In the European Economic Area, the United Kingdom, Switzerland, Canada, Turkey, South Korea, China, India, Russia, Vietnam, Thailand, Indonesia and Saudi Arabia, and whenever the country is not known, the app asks once and sends nothing unless you choose Share. In other countries analytics is on for players aged 16 or older. Either way you can turn it on or off at any time in Settings &gt; Share how you play. For players under 16, analytics is always off. Turning it off stops further collection. Google keeps event data for at most 14 months and then deletes it. Because the data carries only a random identifier and nothing that names you, we cannot pick out which data is yours; if you have a question about it, contact us at the address below.</p>
<h2>Squeeze recordings (optional)</h2>
<p>Players aged 18 or older are asked, once and separately, whether Pop Clinic may record how their fingers move
while they treat their next 50 customers. Only after a yes, the app records, during treatment only: finger positions
and timing on the skin, the touch pressure the phone reports, the tool, the spots and how each one came out, and how
the game reacted (for example how hard the in-game squeeze was). Nothing from menus, the shop or text. Each customer's
recording is sent to FabledLabs' Google Cloud Firestore database in the European Union (the Netherlands), with Google
acting as our processor. A recording carries a random research ID made on your phone and the game version, and no
name, account, device ID, advertising ID or analytics ID; it is not combined with analytics and never used to
identify anyone or for ads. We use the recordings only to make squeezing feel right, and keep them at most 12 months.
The legal basis is your consent. You can stop at any time in Settings &gt; Squeeze recordings, and "Delete my
recordings" there deletes every recording your phone sent. If you no longer have the phone, write to us with the
research ID shown in that screen. You also have the rights of access and complaint to your data protection
authority.</p>
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
    {
        "slug": "sole-clinic",
        "name": "Sole Clinic: Foot Care ASMR",
        "package": "com.fabledlabs.soleclinic",
        "local": "your patient progress, stars, unlocked polish colors, purchases and settings",
        "ads": True,
        "billing": True,
        "extra": """
<h2>Vibration</h2>
<p>The app uses your phone's vibration motor for haptic feedback. You can turn it off in Settings.</p>
""",
    },
    {
        "slug": "clear-ears",
        "name": "Clear Ears: Earwax Clinic",
        "package": "com.fabledlabs.clearears",
        "local": "your patient progress, stars, unlocked items, purchases and settings",
        "ads": True,
        "billing": True,
        "extra": """
<h2>Vibration</h2>
<p>The app uses your phone's vibration motor for haptic feedback. You can turn it off in Settings.</p>
""",
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
             f"<p class='muted'>Developer: FabledLabs &middot; App ID: {a['package']} &middot; Last updated: {a.get('updated', UPDATED)}</p>",
             "<h2>Summary</h2>",
             "<ul><li>No account or sign-up is needed.</li>"
             + ("<li>The app may send gameplay analytics to FabledLabs through Google Analytics, depending on your country and age (see Analytics), and, only if you say yes, recordings of how you squeeze (see Squeeze recordings).</li>" if a.get("analytics") else
                "<li>We (FabledLabs) do not run servers and do not collect, receive or sell your personal data.</li>")
             + f"<li>The app stores {a['local']} only on your device.</li>"
             + ("<li>Ads are provided by Google AdMob, which may collect device data as described below.</li>" if a["ads"] else "")
             + "</ul>",
             "<h2>Data stored on your device</h2>",
             f"<p>The app keeps {a['local']} in its private storage on your device. This data never leaves your device "
             "through us. It is removed when you uninstall the app or clear its data. It may be included in your own "
             "Android device backup if you have backups enabled, which is governed by Google's terms.</p>"]
    if a["extra"]:
        parts.append(a["extra"])
    if a["ads"]:
        parts.append(ADS_SECTION.format(ads_more=a.get("ads_more", ""), remove_ads=a.get("remove_ads", REMOVE_ADS)))
    if a["billing"]:
        parts.append(BILLING_SECTION)
    parts.append(f"\n<h2>Children</h2>\n<p>{a.get('children', CHILDREN)}</p>")
    parts.append("""<h2>Security</h2>
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
    (OUT / "pop-clinic-delete-data.html").write_text(page("Pop Clinic - Delete your data", POP_CLINIC_DELETE), encoding="utf-8")


# Play Console > Data safety > "Delete data URL": the steps to have Pop Clinic data deleted.
POP_CLINIC_DELETE = """<h1>Pop Clinic: delete your data</h1>
<p class='muted'>Developer: FabledLabs &middot; App: Pop Clinic: Satisfying Pops (com.fabledlabs.popclinic)</p>
<p>Pop Clinic has no accounts. What it keeps about you is on your phone, except two things that are sent only with
your choice: gameplay analytics (Google Analytics for Firebase) and, if you said yes, squeeze recordings.</p>
<h2>Squeeze recordings</h2>
<ol>
<li>Open Pop Clinic and tap the gear (Settings).</li>
<li>Tap <b>Squeeze recordings</b>, then <b>Delete my recordings</b>.</li>
</ol>
<p>Every recording your phone sent is deleted from our database, recordings still waiting on the phone are removed,
and recording stops. If you no longer have the phone, write to us (the developer e-mail address on the app's Google Play
page) with the research ID shown in that screen, and we delete them. Recordings are otherwise deleted after at most 12
months.</p>
<h2>Gameplay analytics</h2>
<p>Turn it off in Settings &gt; <b>Share how you play</b>. Analytics events carry only a random app-instance identifier,
so we cannot pick out which data is yours; Google deletes event data after at most 14 months. Uninstalling the app or
clearing its data removes the identifier.</p>
<h2>On your phone</h2>
<p>Your progress, coins, looks, settings and the age you entered stay on your phone. Uninstalling the app or clearing
its data in Android's settings deletes them.</p>
<p><a href='pop-clinic.html'>Full privacy policy</a></p>
"""


if __name__ == "__main__":
    main()
