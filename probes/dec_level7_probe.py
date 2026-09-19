#!/usr/bin/env python3
"""THE DESCENT WALK — the dedicated level-7 gauntlet (v3.1.142, R64).

R63 gave the ascent its own walk; this round the DESCENT gets its own:
--scene level-7 directly (no levels 1-6 tax; the 180s gate cap belongs
to the gauntlet alone) so the law can be proven before the tour grows
HOPS to level-8.

THE AUTOPSY THAT SHAPED THIS LAW (scenes/level-7.dxn1.json + spark.cpp):
  the scene: four fangs ON deck tops (fang-1 on drop-1, fang-2 on the
  shaft-floor, fang-3 on the mid-deck, fang-4 on drop-3) plus the
  floating fang-a at the start ledge's edge, two static hovering saws
  (saw-1 over drop-2's left half, saw-2 over the shaft-floor's right),
  a carousel-saw floating PAST the mid-deck's right edge, two vertical
  movers (lift-1 430<->300 @85 carrying the mid-deck approach,
  vault-lift 400<->480 @65 feeding the vault floor), the magnet at 150
  (the gems collect themselves), the goal on the vault floor.
  THE ENGINE CONTRACT (spark.cpp 306-326, re-read this round): the
  landing resolve snaps on ANY AABB overlap while falling; the ground
  support lasts until the WHOLE body leaves the deck (the walk-off
  fires at hero = deck_right — the drop-2 walk-off lands the body's
  slide INSIDE fang-2's band: the crossing is a JUMP, never a walk);
  the tagless solids block horizontally, movers only vertically (a
  lift can never side-bonk a flight); spikes/hazards kill on the RAW
  box (rot is cosmetic).

THE THREE SOLVERS (the round's machinery):
  1. THE FLOOR SOLVER (drop-2 -> shaft-floor): the fire zone sits
     between saw-1's standing shadow (866..938) and the deck's edge —
     the full-hold landing [1261..1320] slides into saw-2's standing
     shadow (1286..1358) or fang-2's band (1200..1234) for every fire
     in the zone: the PARTIAL HOLD (R63's solver, reused) releases the
     sustained 'd' at t1 so the drag 220/s shaves the drift and
     softens the arrival vx — the landing window [1238, 1268] between
     fang-2's band and saw-2's shadow becomes a law.
  2. THE LIFT-1 BOARD SOLVER (shaft-floor -> lift-1): the stand zone
     [1242, 1264] (the saw-2 ascent rule caps the fire at 1266.4);
     the lift's LOW park (430) is the ONLY reachable plane (the high
     park 300 stands 130px above the launch — 2px over the 128.07px
     jump ceiling) and the catch demands the deck descending: THE
     PHASE GATE (pxi == 0 && y <= 359 — the down leg's top half)
     plus catch_sim_ph (the deck simulated at 5ms against the
     partial-hold drift) — the landing window [1440, 1538] is the
     honest AABB (any-overlap catches) with the slid end <= 1532.
  3. THE STRIP SOLVER (mid-deck -> the strip past fang-3): fang-3
     (1760..1794) plus the carousel-saw's standing shadow (1866+)
     leave the strip [1798, 1836]; the minimum partial-hold drift is
     213px (the drag cannot kill 330 inside the 0.827s flight) so the
     fire zone [1600, 1615] is FORCED (every earlier fire overshoots
     the deck's 1840 edge, every later fire cannot clear fang-3's
     transit) and the release t1 in [0, 0.25] lands [1798, 1830].

  4. THE LIFTJUMP SOLVER (lift-1 -> the mid-deck's left portion): the
     mid-deck's left face (x 1600, y 300..326) is a WALL at hip level
     — the horizontal resolve pins a walking hero at 1566 forever,
     and every right-half fire crosses fang-3's x-window inside its
     band (the wall caps the fire at 1566, the transit demands
     1565..1566 — a 1px lottery). Fire from the lift's LEFT half
     (1460..1489) with the partial hold: the landing [1676, 1712]
     sits BEFORE fang-3, the body's right clears the fang's x-window
     by 48px, the slid end <= 1718 owns the shadow.

THE WALK (eleven bands, first match wins — every fire PREDICTED, a
miss is a held stand or an honest death, never a leap of faith;
the stand-fire drift is the law: every zone fires from a SETTLED
stand, the drift_wd ramp from vx~0 flies 294.8/290.7/286.5 — the
walk-fire windows of the first draft stalled 20-24px short forever):
  START LEDGE (top 140): stand zone 356..380; JUMP-1 (the drop 100 to
    drop-1) lands 648..676 — past fang-1's descent feet-212 crossing
    (the drift 283.2 there binds the zone's floor at 354.8), the
    fang-a's ascent cleared by construction (the body exits its
    y-band at t=0.045 with the box right <= 416).
  DROP-1 (top 240): brake; stand zone 679..709; JUMP-2 (the drop 90
    to drop-2) lands 966..1000 — the descent's feet-268 crossing past
    saw-1's x (>= 942), the ascent's feet-306 crossing left of it.
  DROP-2 (top 330): brake; stand zone 943..1002 (past saw-1's
    shadow); JUMP-3 = THE FLOOR SOLVER.
  SHAFT-FLOOR (top 430): brake; stand zone 1242..1264 (the saw-2
    ascent rule caps the fire at 1266.4 — the pre-release drift at
    the feet-368 crossing is 15.6, the body's right fire+49.6);
    JUMP-4 = THE LIFT-1 BOARD SOLVER (the phase gate owns the deck's
    descent; the landing window [1440, 1538] is the honest AABB —
    any-overlap catches, the slid end <= 1532).
  LIFT-1 RIDER: brake; patrol into 1460..1489 (the lift's LEFT half);
    JUMP-5 = THE LIFTJUMP SOLVER fires near the cycle top (the deck
    300..314) with the partial hold and lands [1676, 1712] BEFORE
    fang-3 — the wall and the transit are both dodged by altitude
    and by never entering the fang's x-window.
  MID-DECK (top 300): brake; patrol LEFT into 1600..1615; JUMP-6 =
    THE STRIP SOLVER (the release t1 lands [1798, 1830] past
    fang-3's transit, the slid end <= 1836).
  THE STRIP (mid-deck's right, past fang-3): brake; stand zone
    1800..1828; JUMP-7 (the drop 80 to drop-3's 380, the FULL hold)
    lands 2086..2138 — the carousel-saw cleared BOTH ways (the
    ascent's feet-278 crossing <= 1896, the descent's feet-240
    crossing past 1942), the arrival slide stops before fang-4's
    standing shadow (2166).
  DROP-3 (top 380): brake; stand zone 2070..2150 (the fang-4 rise
    rule caps the fire at 2150); JUMP-8 fires on catch_sim (any deck
    pose — the feet sweep the lift's whole 400..480 range while the
    box stays inside the 2360..2460 span) and lands ON vault-lift.
  VAULT-LIFT RIDER: brake; creep right into 2396..2426; JUMP-9 (the
    goal jump, any deck pose) lands 2660..2722 on the vault floor —
    the goal's x-band (2760..2790) is touched by the walk-in (the
    receipt decides, the machine never overrides it).
  VAULT FLOOR (top 480): walk right into the goal.
The tour ends the moment the level-8 receipt lands — the machine
decides when it's done."""
import os as _os
_HOME = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os, pty, re, select, sys, tempfile, time

REPO = _HOME
BIN = os.path.join(REPO, "native", "build", "dxn3-native")

DEST = "level-8"                  # the receipt that ends the walk
CAP = 170.0                       # wall cap (gate 8 kills probes at 180)

tfd, TRACE = tempfile.mkstemp(prefix="dxn3_l7_", suffix=".trace")
os.close(tfd)

DIRTY0 = _os.popen(f"git -C {REPO!r} status --porcelain").read()

pid, fd = pty.fork()
if pid == 0:
    os.chdir(REPO)
    os.environ["TERM"] = "xterm-256color"
    os.environ["DXN3_TRACE"] = TRACE
    os.environ["DXN3_TRACE_MS"] = "25"
    os.execv(BIN, [BIN, "--scene", "scenes/level-7.dxn1.json"])
    os._exit(1)

buf = b""
def drainf(seconds):
    global buf
    end = time.time() + seconds
    while time.time() < end:
        r, _, _ = select.select([fd], [], [],
                                min(0.004, max(0.001, end - time.time())))
        if r:
            try: chunk = os.read(fd, 1 << 16)
            except OSError: return False
            if not chunk: return False
            buf += chunk
    return True

def send(s): os.write(fd, s if isinstance(s, bytes) else s.encode())

LINE = re.compile(rb"w=\s*([\d.]+) f=\s*\d+ s=\s*(\d+)[^\n]*px=(-?[\d.]+) py=(-?[\d.]+) "
                  rb"vx=(-?[\d.]+) vy=(-?[\d.]+)")
MOVERL = re.compile(rb"MOVER n=(\S+) x=(-?[\d.]+) y=(-?[\d.]+) pxi=(\d+) dir=(-?\d+)")
WELCOME = re.compile(rb"EVENT shell: welcome to (.+?)\s*$", re.M)
RESPAWN = re.compile(rb"^  EVENT respawn", re.M)

def hop_hit(name, key):
    if isinstance(name, bytes):
        name = name.decode(errors="replace")
    return name == key or name.endswith("(" + key + ")")

class TraceTail:
    """the tail law (grand_tour's): new bytes only, the newest sample
    kept — plus the RESPAWN EYE: every 'EVENT respawn' line bumps a
    counter the decision reads (a death mid-flight must clear the
    flight latch even when the spawn sits < 400px from the pit)."""
    def __init__(self, path):
        self.path = path; self.pos = 0; self.tail = b""
        self.last = None
        self.welcome = None
        self.movers = {}
        self.respawns = 0
    def pump(self):
        try:
            with open(self.path, "rb") as f:
                f.seek(self.pos)
                chunk = f.read()
        except OSError:
            return
        if not chunk: return
        self.pos += len(chunk)
        self.tail += chunk
        lines = self.tail.split(b"\n")
        self.tail = lines.pop()
        for ln in lines:
            m = LINE.search(ln)
            if m:
                self.last = (m.group(1), int(m.group(2)), float(m.group(3)),
                             float(m.group(4)), float(m.group(5)),
                             float(m.group(6)))
            elif ln.startswith(b"  MOVER"):
                mm = MOVERL.search(ln)
                if mm:
                    self.movers[mm.group(1).decode()] = (
                        float(mm.group(2)), float(mm.group(3)),
                        int(mm.group(4)), int(mm.group(5)))
            elif ln.startswith(b"  EVENT"):
                wm = WELCOME.search(ln)
                if wm:
                    self.welcome = wm.group(1).decode()
                if RESPAWN.match(ln):
                    self.respawns += 1

def trace_text():
    try:
        with open(TRACE, "rb") as f: return f.read()
    except OSError:
        return b""

tail = TraceTail(TRACE)

# ---- the constants (scenes/level-7.dxn1.json + native/src/spark.hpp) ----
G, JUMPV, RACCEL, RUNMAX = 1500.0, 620.0, 2300.0, 330.0
AIR_DRAG = 220.0                  # AIR_FRICTION: the no-input decay /s
HERO_W = 34.0

def dbg(tag, x, y, vx, note=""):
    if _os.environ.get("DXN3_L7_DEBUG"):
        print(f"[L7-{tag}] x={x:.0f} y={y:.0f} vx={vx:.0f} {note}",
              file=sys.stderr, flush=True)

def drift_wd(t, vx):
    """the held-'d' drift over t: the exact RUN_ACCEL ramp from the live
    vx to the 330 cap (the flight hold delivers every px of this)."""
    if vx >= RUNMAX:
        return RUNMAX * t
    tt = (RUNMAX - vx) / RACCEL
    if t <= tt:
        return vx * t + 0.5 * RACCEL * t * t
    return vx * tt + 0.5 * RACCEL * tt * tt + RUNMAX * (t - tt)

def drift_ph(t, t1, vx):
    """the PARTIAL-HOLD drift: the sustained 'd' until t1 (the exact
    ramp), then released — the AIR_DRAG 220/s owns the rest (the code
    path: dir==0 -> AIR_FRICTION*dt; the vx decays linearly, the drift
    gains v1*(t-t1) - 110*(t-t1)^2). THE STOP CLAMP (the stand-fire
    law): the decay ends at v1/220 — the engine's own friction clamps
    at vx == 0 (`if abs(vx) <= fr: vx = 0`), so the tail integrates
    only to the stop. THE PRE-RELEASE BRANCH (the second red's
    autopsy): a crossing BEFORE the release (t < t1 — the lift-1
    board's saw-2 ascent at t=0.1164 against a t1=0.3 hold) flies
    drift_wd(t, vx) — the hold is still SUSTAINED there; returning
    drift_wd(t1) overstated the drift by 60px and the (a) gate
    rejected every honest candidate for 100 seconds."""
    if t <= t1:
        return drift_wd(t, vx)
    d = drift_wd(t1, vx)
    v1 = min(RUNMAX, vx + RACCEL * t1)
    dt = min(t - t1, v1 / AIR_DRAG)
    return d + v1 * dt - 0.5 * AIR_DRAG * dt * dt

def arc_t(rise):
    """the DESCENT time at which the arc's feet cross `rise` px above
    the launch (a negative rise = a drop, the formula holds); None if
    the plane sits above the apex (rise > JUMPV^2/(2G) = 128.07)."""
    d = JUMPV * JUMPV - 2.0 * G * rise
    if d < 0.0:
        return None
    return (JUMPV + d ** 0.5) / G

def arc_t_asc(rise):
    """the ASCENT time of the same crossing (the small root); None if
    the plane sits above the apex."""
    d = JUMPV * JUMPV - 2.0 * G * rise
    if d < 0.0:
        return None
    return (JUMPV - d ** 0.5) / G

def catch_sim(wp, speed, axis, plane_fixed, pos, tgt, feet0, x0, vx0,
              span_lo, span_w, tmax=1.7, dt=0.005):
    """THE HONEST CATCH — the moving-deck landing, simulated.

    wp = the deck's two waypoint coords on its axis (in path order),
    speed = pspeed, pos = the live coord, tgt = the waypoint index the
    deck heads to (the telemetry's pxi). axis 'y': the deck's plane is
    its own y (the span check uses the FIXED x extent [span_lo,
    +span_w]); axis 'x': the plane is plane_fixed (unused here) and
    the span MOVES with the deck.

    The hero: feet(t) = feet0 - 620t + 750t^2, x(t) = x0 + drift_wd(t,
    vx0) — the flight hold delivers every px. Steps 5ms: the first
    DESCENT crossing (the feet come onto the plane from above) with the
    landing box on the deck's span is THE LANDING; an ascent crossing
    with the box over the span is THE BONK (the resolve snaps him below
    — the deck is lost) and rejects the fire.
    Returns (t_land, land_x, deck_pos_at_land, bonk)."""
    return _catch_core(wp, speed, axis, plane_fixed, pos, tgt, feet0,
                       x0, vx0, span_lo, span_w, None, tmax, dt)

def catch_sim_ph(wp, speed, axis, plane_fixed, pos, tgt, feet0, x0, vx0,
                 span_lo, span_w, t1, tmax=1.7, dt=0.005):
    """THE PARTIAL-HOLD CATCH — catch_sim with the release: the drift
    is drift_ph(t, t1, vx0) (the sustained 'd' until t1, then the
    AIR_DRAG owns the tail — the exact code path). Everything else
    identical."""
    return _catch_core(wp, speed, axis, plane_fixed, pos, tgt, feet0,
                       x0, vx0, span_lo, span_w, t1, tmax, dt)

def _catch_core(wp, speed, axis, plane_fixed, pos, tgt, feet0, x0, vx0,
                span_lo, span_w, t1, tmax, dt):
    t = 0.0
    plane0 = pos if axis == "y" else plane_fixed
    prev_above = (plane0 - feet0) > 0.0
    bonk = False
    x = x0
    while t < tmax:
        t += dt
        tc = wp[tgt]                       # the deck advances toward its
        d = tc - pos                       # waypoint, bouncing at the
        if abs(d) <= speed * dt:           # ends (the engine's own law)
            pos = tc; tgt = 1 - tgt
        else:
            pos += speed * dt if d > 0.0 else -speed * dt
        feet = feet0 - JUMPV * t + 0.5 * G * t * t
        x = x0 + (drift_wd(t, vx0) if t1 is None
                  else drift_ph(t, t1, vx0))
        plane = pos if axis == "y" else plane_fixed
        above = (plane - feet) > 0.0       # the hero above the deck's top
        slo = span_lo if axis == "y" else pos
        on = x < slo + span_w and x + HERO_W > slo
        if prev_above and not above:       # the descent crossing
            if on:
                return (t, x, pos, bonk)
        elif prev_above is False and above:  # the ascent crossing
            if on:
                return (None, x, pos, True)
        prev_above = above
    return (None, x, pos, bonk)


# ---- the descent's movers (scenes/level-7.dxn1.json, path order) --------
L1_WP, L1_SP, L1_LO, L1_W = (430.0, 300.0), 85.0, 1460.0, 110.0
VL_WP, VL_SP, VL_LO, VL_W = (400.0, 480.0), 65.0, 2360.0, 100.0


class St:
    __slots__ = ("last_x", "last_jump", "flight", "hold", "fire_s",
                 "fire_vx", "fire_t", "hold_t", "seen_r")

    def __init__(self):
        self.last_x = None; self.last_jump = 0.0
        self.flight = False; self.hold = b"d"; self.fire_s = -1
        self.fire_vx = 0.0
        self.fire_t = 0.0            # the fire's predicted flight time
        self.hold_t = 0.0            # THE PARTIAL HOLD's release time
        self.seen_r = 0


def common_reset(st, h):
    x = h[2]
    if st.last_x is not None and abs(x - st.last_x) > 400:
        st.flight = False
        st.last_x = None
        return True
    return False


def floor_solve(x, vx, feet):
    """SOLVER 1 (drop-2 -> shaft-floor): search the release t1 on a
    10ms grid; every candidate must pass ALL of —
      (a) the saw-2 transit: the box's right edge at the descent's
          feet-406 crossing (the band's exit — the binding edge, the
          drift only grows) stays <= 1316 (4px inside the saw's 1320);
      (b) the landing window [1238, 1268] (past fang-2's 1234 band,
          left of saw-2's 1286 standing shadow);
      (c) the arrival slide: the brake slide varr^2/4600 keeps the
          slid end <= 1280 (6px inside the shadow);
      (d) the arrival vx >= 40 (a dead stall is not a landing).
    Returns the best-margin (t1, t_land, t406, L, varr) or None."""
    t_land = arc_t(feet - 430.0)
    if t_land is None:
        return None
    t406 = arc_t(feet - 406.0)
    if t406 is None or t406 > t_land:
        t406 = t_land
    best = None
    n = int((t_land - 0.05 - 0.20) / 0.01) + 1
    for i in range(max(0, n)):
        t1 = 0.20 + i * 0.01
        if t1 > t_land - 0.05:
            break
        clr = x + drift_ph(t406, t1, vx) + 34.0
        if clr > 1316.0:
            continue                 # (a) fails; a longer hold only
                                     # raises the transit drift, so
                                     # keep searching upward
        L = x + drift_ph(t_land, t1, vx)
        if not (1238.0 <= L <= 1268.0):
            continue                 # (b)
        varr = min(RUNMAX, vx + RACCEL * t1) - AIR_DRAG * (t_land - t1)
        if varr < 40.0:
            continue                 # (d)
        end = L + varr * varr / 4600.0 + 2.0
        if end > 1280.0:
            continue                 # (c)
        score = min(1316.0 - clr, 1268.0 - L, L - 1238.0, 1280.0 - end)
        if best is None or score > best[0]:
            best = (score, t1, t_land, t406, L, varr)
    if best is None:
        return None
    return best[1:]


def lift1_solve(x, vx, feet, l1):
    """SOLVER 2 (shaft-floor -> lift-1): search the release t1 on a
    10ms grid; every candidate must pass ALL of —
      (a) the saw-2 ascent: the box's right edge at the ascent's
          feet-368 crossing (the band's exit — the binding edge)
          stays <= 1316;
      (b) THE HONEST CATCH: catch_sim_ph puts the box on lift-1's span
          at the descent crossing (no bonk) with the landing window
          [1440, 1538] — the AABB catch is any-overlap, so the honest
          left edge is the body's right past the deck's 1460 by 14px;
          the slid end keeps the box on the deck through the brake
          (end <= 1532, the body's right 4px inside the 1570 edge);
      (c) the arrival vx >= 40.
    Returns the best-margin (t1, t_land, L, varr) or None."""
    ta368 = arc_t_asc(feet - 368.0)
    if ta368 is None:
        return None
    best = None
    for i in range(101):
        t1 = i * 0.01
        clr = x + drift_ph(ta368, t1, vx) + 34.0
        if clr > 1316.0:
            continue                 # (a)
        t, land, dpos, bonk = catch_sim_ph(
            L1_WP, L1_SP, "y", 0.0, l1[1], l1[2], feet, x, vx,
            L1_LO, L1_W, t1)
        if t is None or bonk or not (1440.0 <= land <= 1538.0):
            continue                 # (b)
        t_hold = min(t, t1)
        varr = min(RUNMAX, vx + RACCEL * t_hold) - \
            AIR_DRAG * max(0.0, t - t1)
        if varr < 40.0:
            continue                 # (c)
        end = land + varr * varr / 4600.0 + 2.0
        if end > 1532.0:
            continue                 # (b2) the slid end stays on the deck
        score = min(1316.0 - clr, 1538.0 - land, land - 1440.0,
                    1532.0 - end)
        if best is None or score > best[0]:
            best = (score, t1, t, land, varr)
    if best is None:
        return None
    return best[1:]


def liftjump_solve(x, vx, feet):
    """SOLVER 4 (lift-1 -> the mid-deck's left portion): the mid-deck's
    left face (x 1600, y 300..326) is a WALL at hip level — the third
    red's autopsy: the walk-off pins the hero at 1566 forever (the
    horizontal resolve pushes him back every frame while his body
    spans the wall's y-band), and a right-half fire crosses fang-3's
    x-window (1726..1794) with the feet inside its band for every
    reachable fire x (the wall caps the fire at 1566; the transit
    demands 1565..1566 — a 1px lottery). THE HONEST PATH: fire from
    the lift's LEFT half (1460..1489, no wall, no transit) with the
    PARTIAL HOLD: the landing [1676, 1712] sits BEFORE fang-3 (the
    body's right at the feet-272 crossing stays <= 1756, 4px clear of
    the fang's 1760) and the arrival slide stops before fang-3's
    standing shadow (1726). Search the release t1 on a 10ms grid —
      (a) the landing window [1676, 1712];
      (b) the slid end <= 1718 (4px inside the shadow);
      (c) the fang-3 transit: the body's right at the descent's
          feet-272 crossing <= 1756;
      (d) the arrival vx >= 40.
    Returns the best-margin (t1, t_land, L, varr) or None."""
    t_land = arc_t(feet - 300.0)
    if t_land is None:
        return None
    t272 = arc_t(feet - 272.0)
    if t272 is None or t272 > t_land:
        t272 = t_land
    best = None
    n = int(min(0.65, t_land - 0.05) / 0.01) + 1
    for i in range(max(0, n)):
        t1 = i * 0.01
        L = x + drift_ph(t_land, t1, vx)
        if not (1676.0 <= L <= 1712.0):
            continue                 # (a)
        varr = min(RUNMAX, vx + RACCEL * t1) - AIR_DRAG * (t_land - t1)
        if varr < 40.0:
            continue                 # (d)
        end = L + varr * varr / 4600.0 + 2.0
        if end > 1718.0:
            continue                 # (b)
        clr = x + drift_ph(t272, t1, vx) + 34.0
        if clr > 1756.0:
            continue                 # (c)
        score = min(1712.0 - L, L - 1676.0, 1718.0 - end, 1756.0 - clr)
        if best is None or score > best[0]:
            best = (score, t1, t_land, L, varr)
    if best is None:
        return None
    return best[1:]


def strip_solve(x, vx, feet):
    """SOLVER 3 (mid-deck -> the strip past fang-3): search the release
    t1 on a 10ms grid; every candidate must pass ALL of —
      (a) the fang-3 transit: the box's left edge at the descent's
          feet-272 crossing (the band's entry — the binding edge) is
          already past the fang's 1794;
      (b) the landing window [1798, 1830] (the strip: past fang-3's
          band, left of the deck's 1840 edge by the slide room);
      (c) the arrival slide keeps the slid end <= 1836;
      (d) the arrival vx >= 40.
    Returns the best-margin (t1, t_land, t272, L, varr) or None."""
    t_land = arc_t(feet - 300.0)
    if t_land is None:
        return None
    t272 = arc_t(feet - 272.0)
    if t272 is None or t272 > t_land:
        t272 = t_land
    best = None
    n = int(min(0.25, t_land - 0.05) / 0.01) + 1
    for i in range(max(0, n)):
        t1 = i * 0.01
        clr = x + drift_ph(t272, t1, vx)
        if clr < 1794.0:
            continue                 # (a) fails; a longer hold only
                                     # raises the transit drift, so
                                     # keep searching upward
        L = x + drift_ph(t_land, t1, vx)
        if not (1798.0 <= L <= 1830.0):
            continue                 # (b)
        varr = min(RUNMAX, vx + RACCEL * t1) - AIR_DRAG * (t_land - t1)
        if varr < 40.0:
            continue                 # (d)
        end = L + varr * varr / 4600.0 + 2.0
        if end > 1836.0:
            continue                 # (c)
        score = min(clr - 1794.0, 1830.0 - L, L - 1798.0, 1836.0 - end)
        if best is None or score > best[0]:
            best = (score, t1, t_land, t272, L, varr)
    if best is None:
        return None
    return best[1:]


def dec_level7(h, st, now):
    # THE RESPAWN EYE: a death resets the flight latch even when the
    # spawn sits < 400px from the pit (the position jump alone can lie)
    if tail.respawns != st.seen_r:
        st.seen_r = tail.respawns
        st.flight = False
        st.last_x = None
        return b""
    if common_reset(st, h):
        st.last_x = h[2]; st.flight = False
        return b"d"
    w, s, x, y, vx, vy = h
    grounded = abs(vy) < 1.0
    feet = y + 44.0
    fire = now - st.last_jump > 0.6

    # THE FLIGHT LATCH: the fire's sustained hold — the drift the
    # prediction assumed, delivered (b"" would let the 220 air friction
    # steal it). THE PARTIAL HOLD: the hold ends at st.hold_t (the
    # solver's release), then b"" — the drag owns the tail exactly as
    # the prediction computed. THE STALE-SAMPLE GUARD (the R58 law):
    # the telemetry trails the engine by up to 25ms, so the sample
    # right after a fire still reads GROUNDED — the latch clears only
    # on a landing sample newer than the fire by a 10-step margin.
    if st.flight:
        if grounded and s > st.fire_s + 10:
            st.flight = False
        elif grounded and s > st.fire_s + 4 and \
                vx > st.fire_vx + 120.0:
            # THE EATEN-W EYE (R60): grounded samples at +5..+10 whose
            # vx is RUNNING AWAY (the held 'd' adds +57px/s per line)
            # are PROOF the fire's 'w' never reached the engine.
            st.flight = False
        elif now - st.last_jump < st.hold_t:
            return st.hold           # the sustained hold
        else:
            return b""               # the released tail (the drag law)

    # ---- 1. THE START LEDGE (top 140, stand py 96, x <= 420): stand
    # zone 356..380 (THE STAND-FIRE DRIFT: the settle fires from vx~0,
    # the drift_wd ramp from zero flies 294.8 — the walk-fire window
    # [330, 352] would land 24px short of the gate and stall forever,
    # the first red's autopsy); JUMP-1 (the drop 100 to drop-1's 240)
    # lands 648..676 — past fang-1's descent feet-212 crossing (>= 638:
    # the drift 283.2 at the crossing puts the binding at 354.8) and
    # the slid end stays <= 700 (44px inside the deck's 740 edge); the
    # fang-a's ascent is cleared by construction (the body exits its
    # y-band at t=0.045 with the box right <= 416, 34px left of it).
    if grounded and 85 <= y <= 108 and x <= 424:
        st.last_x = x
        if x > 380:
            return b"a" if vx > -150 else b""
        if x < 356:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 60.0:
            return b""               # the settle: the fire waits for
                                     # a stand
        t = arc_t(feet - 240.0)
        if t is None:
            return b""
        land = x + drift_wd(t, vx)
        t212 = arc_t(feet - 212.0)
        clr = x + drift_wd(t212, vx) if t212 is not None else 1e9
        if 648.0 <= land <= 676.0 and clr >= 638.0:
            dbg("ledge-jump", x, y, vx, f"t={t:.2f} land={land:.0f} "
                f"clr={clr:.0f}")
            st.last_jump = now; st.fire_s = s; st.fire_vx = vx
            st.flight = True; st.fire_t = t; st.hold_t = t; st.hold = b"d"
            return b"wd"
        return b""

    # ---- 2. DROP-1 (top 240, stand py 196, x 520..740): brake the
    # arrival (the slid end stays <= 700, the 740 edge owned); stand
    # zone 679..709 (the stand-fire drift 290.7 — the walk-fire window
    # [655, 684] stalls 20px short of the gate; the feet-268 crossing
    # binding sits at 678.6); JUMP-2 (the drop 90 to drop-2's 330)
    # lands 966..1000 — the descent's feet-268 crossing past saw-1's
    # x (>= 942), the ascent's feet-306 crossing left of the saw (the
    # box right <= 896), the arrival slide past the saw's standing
    # shadow (866..938).
    if grounded and 186 <= y <= 206 and 520 <= x <= 740:
        st.last_x = x
        if vx > 40:
            return b"a"              # THE ARRIVAL BRAKE
        if x > 709:
            return b"a" if vx > -150 else b""
        if x < 679:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 60.0:
            return b""
        t = arc_t(feet - 330.0)
        if t is None:
            return b""
        land = x + drift_wd(t, vx)
        t268 = arc_t(feet - 268.0)
        clr = x + drift_wd(t268, vx) if t268 is not None else 1e9
        ta306 = arc_t_asc(feet - 306.0)
        xe = x + drift_wd(ta306, vx) + 34.0 if ta306 is not None else 1e9
        if 966.0 <= land <= 1000.0 and clr >= 942.0 and xe <= 896.0:
            dbg("drop1-jump", x, y, vx, f"t={t:.2f} land={land:.0f} "
                f"clr={clr:.0f} xe={xe:.0f}")
            st.last_jump = now; st.fire_s = s; st.fire_vx = vx
            st.flight = True; st.fire_t = t; st.hold_t = t; st.hold = b"d"
            return b"wd"
        return b""

    # ---- 3. DROP-2 (top 330, stand py 286, x 840..1040): brake the
    # arrival (the slid end stays <= 1022, past saw-1's standing
    # shadow 866..938); stand zone 943..1002 (5px clear of the
    # shadow, 38px inside the deck's edge); JUMP-3 = THE FLOOR SOLVER
    # (the partial hold lands [1238, 1268] between fang-2's band and
    # saw-2's standing shadow — the full hold cannot: the saw-2
    # shadow or fang-2's band eats every deep landing).
    if grounded and 276 <= y <= 296 and 840 <= x <= 1040:
        st.last_x = x
        if vx > 40:
            return b"a"
        if x > 1002:
            return b"a" if vx > -150 else b""
        if x < 943:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 30.0:
            return b""               # the tighter settle: the partial
                                     # hold's margins live on the live vx
        r = floor_solve(x, vx, feet)
        if r is None:
            return b""
        t1, t_land, t406, L, varr = r
        dbg("floor-fire", x, y, vx,
            f"feet={feet:.0f} t1={t1:.2f} tland={t_land:.2f} L={L:.0f} "
            f"varr={varr:.0f}")
        st.last_jump = now; st.fire_s = s; st.fire_vx = vx
        st.flight = True; st.fire_t = t_land; st.hold_t = t1; st.hold = b"d"
        return b"wd"

    # ---- 4. THE SHAFT-FLOOR (top 430, stand py 386, x 1120..1380):
    # brake the arrival (the slid end stays <= 1150, fang-2's 1166
    # shadow owned); stand zone 1242..1264 (the saw-2 ascent rule caps
    # the fire at 1266.4 — the body's right at the feet-368 crossing
    # is fire+49.6 with the fixed pre-release drift — and the
    # floor-fire's own arrival stops at ~1263, inside); JUMP-4 = THE
    # LIFT-1 BOARD SOLVER:
    # THE PHASE GATE first (pxi == 0 — the deck heads DOWN to its 430
    # park — and y <= 359, the down leg's top half: the deck's live
    # top at the touchdown lands in the catchable 370..430 band; a
    # fire on the up leg meets the deck 70px higher — the park catch
    # misses by 6px and the hero falls into the 1380..1460 gap).
    if grounded and 376 <= y <= 396 and 1120 <= x <= 1380:
        st.last_x = x
        l1 = tail.movers.get("lift-1")
        if vx > 40:
            return b"a"
        if x > 1264:
            return b"a" if vx > -150 else b""
        if x < 1242:
            return b"d" if vx < 150 else b""
        if l1 is None or not fire or abs(vx) > 30.0:
            return b""
        if l1[2] != 0 or l1[1] > 359.0:
            return b""               # THE PHASE GATE: the deck's
                                     # descent only (see the header)
        r = lift1_solve(x, vx, feet, l1)
        if r is None:
            return b""
        t1, t_land, L, varr = r
        dbg("lift1-board", x, y, vx,
            f"s={s} l1={l1[1]:.0f} pxi={l1[2]} t1={t1:.2f} "
            f"tland={t_land:.2f} L={L:.0f} varr={varr:.0f}")
        st.last_jump = now; st.fire_s = s; st.fire_vx = vx
        st.flight = True; st.fire_t = t_land; st.hold_t = t1; st.hold = b"d"
        return b"wd"

    # ---- 5. LIFT-1 RIDER (deck 1460..1570, ride py 256..386): brake
    # the arrival; patrol left into the fire zone 1460..1489 (the lift's
    # LEFT half — the third red's autopsy: the mid-deck's left face is
    # a WALL at hip level, the walk-off pins the hero at 1566 forever,
    # and every right-half fire crosses fang-3's x-window inside its
    # band — the wall caps the fire at 1566 and the transit demands
    # 1565..1566, a 1px lottery); JUMP-5 = THE LIFTJUMP SOLVER fires
    # near the cycle top (the deck 300..314) with the PARTIAL HOLD and
    # lands [1676, 1712] BEFORE fang-3 — the body's right clears the
    # fang's x-window by 48px and the arrival slide stops 4px inside
    # fang-3's standing shadow (1726).
    if grounded and 1455 <= x <= 1575 and 248 <= y <= 392:
        st.last_x = x
        l1 = tail.movers.get("lift-1")
        if vx > 40:
            return b"a"
        if x > 1489:
            return b"a" if vx > -150 else b""
        if x < 1460:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 60.0:
            return b""
        if l1 is None or not (300.0 <= l1[1] <= 314.0):
            return b""               # THE HIGH-HALF GATE: the deck
                                     # 300..314 only (the rise to the
                                     # mid-deck's plane stays <= 14)
        r = liftjump_solve(x, vx, feet)
        if r is None:
            return b""
        t1, t_land, L, varr = r
        dbg("lift-jump", x, y, vx,
            f"s={s} l1={l1[1]:.0f} t1={t1:.2f} tland={t_land:.2f} "
            f"L={L:.0f} varr={varr:.0f}")
        st.last_jump = now; st.fire_s = s; st.fire_vx = vx
        st.flight = True; st.fire_t = t_land; st.hold_t = t1; st.hold = b"d"
        return b"wd"

    # ---- 6. THE MID-DECK (top 300, stand py 256, x 1600..1840):
    # brake the arrival (the lift-jump lands [1676, 1712] with the
    # slid end <= 1718, fang-3's standing shadow owned); patrol LEFT
    # into the stand zone 1600..1615 (the strip is FORCED by the
    # minimum partial-hold drift: the instant release still flies
    # 213px, every earlier fire overshoots the deck's 1840 edge);
    # JUMP-6 = THE STRIP SOLVER (the release t1 lands
    # [1798, 1830] past fang-3's transit).
    if grounded and 246 <= y <= 266 and 1560 <= x <= 1740:
        st.last_x = x
        if vx > 40:
            return b"a"
        if x > 1615:
            return b"a" if vx > -150 else b""
        if x < 1600:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 30.0:
            return b""
        r = strip_solve(x, vx, feet)
        if r is None:
            return b""
        t1, t_land, t272, L, varr = r
        dbg("strip-fire", x, y, vx,
            f"feet={feet:.0f} t1={t1:.2f} tland={t_land:.2f} L={L:.0f} "
            f"varr={varr:.0f}")
        st.last_jump = now; st.fire_s = s; st.fire_vx = vx
        st.flight = True; st.fire_t = t_land; st.hold_t = t1; st.hold = b"d"
        return b"wd"

    # ---- 7. THE STRIP (mid-deck's right, stand py 256, x 1796..1844):
    # brake the arrival (the slid end stays <= 1841, the 1840 edge
    # owned by the solver's slid-end gate); stand zone 1800..1828;
    # JUMP-6 (the drop 80 to drop-3's 380, the FULL hold) lands
    # 2086..2138 (the stand-fire drift 286.5 — the deep window's cap
    # is fang-4's standing shadow: the slid end 2138+23.7 = 2161.7,
    # 4px inside the shadow's 2166) — the carousel-saw cleared BOTH
    # ways (the ascent's feet-278 crossing <= 1896, the descent's
    # feet-240 crossing past 1942).
    if grounded and 246 <= y <= 266 and 1796 <= x <= 1844:
        st.last_x = x
        if vx > 40:
            return b"a"
        if x > 1828:
            return b"a" if vx > -150 else b""
        if x < 1800:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 60.0:
            return b""
        t = arc_t(feet - 380.0)
        if t is None:
            return b""
        land = x + drift_wd(t, vx)
        ta278 = arc_t_asc(feet - 278.0)
        xe = x + drift_wd(ta278, vx) + 34.0 if ta278 is not None else 1e9
        td240 = arc_t(feet - 240.0)
        xd = x + drift_wd(td240, vx) if td240 is not None else 1e9
        if 2086.0 <= land <= 2138.0 and xe <= 1896.0 and xd >= 1942.0:
            dbg("strip-jump", x, y, vx, f"t={t:.2f} land={land:.0f} "
                f"xe={xe:.0f} xd={xd:.0f}")
            st.last_jump = now; st.fire_s = s; st.fire_vx = vx
            st.flight = True; st.fire_t = t; st.hold_t = t; st.hold = b"d"
            return b"wd"
        return b""

    # ---- 8. DROP-3 (top 380, stand py 336, x 2060..2280): brake the
    # arrival (the slid end stays <= 2162, fang-4's 2166 shadow
    # owned); stand zone 2070..2150 (the fang-4 rise rule caps the
    # fire at 2150: the body exits the fang's y-band at t=0.045 with
    # the box right <= 2200 only from there); JUMP-7 fires on
    # catch_sim — ANY deck pose works (the feet sweep the lift's whole
    # 400..480 range while the box stays inside the 2360..2460 span).
    if grounded and 326 <= y <= 346 and 2060 <= x <= 2280:
        st.last_x = x
        vl = tail.movers.get("vault-lift")
        if vx > 40:
            return b"a"
        if x > 2150:
            return b"a" if vx > -150 else b""
        if x < 2070:
            return b"d" if vx < 150 else b""
        if vl is None or not fire or abs(vx) > 60.0:
            return b""
        t, land, dpos, bonk = catch_sim(
            VL_WP, VL_SP, "y", 0.0, vl[1], vl[2], feet, x, vx,
            VL_LO, VL_W)
        if t is not None and not bonk and 2372.0 <= land <= 2452.0:
            dbg("vault-board", x, y, vx,
                f"s={s} vl={vl[1]:.0f} pxi={vl[2]} t={t:.2f} "
                f"land={land:.0f} deck={dpos:.0f}")
            st.last_jump = now; st.fire_s = s; st.fire_vx = vx
            st.flight = True; st.fire_t = t; st.hold_t = t; st.hold = b"d"
            return b"wd"
        return b""

    # ---- 9. VAULT-LIFT RIDER (deck 2360..2460, ride py 356..436):
    # brake the arrival; creep right into 2396..2426; JUMP-8 (the goal
    # jump, any deck pose — the drop 0..80 to the floor's 480) lands
    # 2680..2722 on the vault floor — the goal's x-band (2760..2790)
    # is touched by the walk-in (the receipt decides, the machine
    # never overrides it).
    if grounded and 2355 <= x <= 2465 and 350 <= y <= 440:
        st.last_x = x
        if vx > 40:
            return b"a"
        if x > 2426:
            return b"a" if vx > -150 else b""
        if x < 2396:
            return b"d" if vx < 150 else b""
        if not fire or abs(vx) > 60.0:
            return b""
        t = arc_t(feet - 480.0)
        if t is None:
            return b""
        land = x + drift_wd(t, vx)
        if land >= 2600.0:
            dbg("goal-jump", x, y, vx, f"t={t:.2f} land={land:.0f}")
            st.last_jump = now; st.fire_s = s; st.fire_vx = vx
            st.flight = True; st.fire_t = t; st.hold_t = t; st.hold = b"d"
            return b"wd"
        return b""

    # ---- 10. THE VAULT FLOOR (top 480, stand py 436, x 2500..2800):
    # walk right into the goal — the receipt decides when the descent
    # is done.
    if grounded and 426 <= y <= 446 and 2500 <= x <= 2800:
        st.last_x = x
        return b"d"

    # ---- 11. THE DEFAULT (any unbanded state): walk right — a
    # short-sitting hero feeds a fang honestly (the respawn is the
    # recovery; the saws and the void do the rest).
    st.last_x = x
    return b"d"


# ---- the walk itself -----------------------------------------------------
t0 = time.time()
alive = drainf(3.0)
scene = None
st = St()
while time.time() - t0 < CAP:
    tail.pump()                    # THE TAIL: new bytes only
    if tail.welcome and tail.welcome != scene:
        scene = tail.welcome
        st = St()
        tail.movers.clear()        # the new scene's decks speak for it
        if hop_hit(scene, DEST):
            break                  # THE MACHINE DECIDES: the descent is
                                   # crossed when level-8's receipt lands
    h = tail.last
    if h:
        key = dec_level7(h, st, time.time())
        if key: send(key)
    if not drainf(0.0025):
        break
drainf(1.2)                        # the last load + its first frames
tr = trace_text()

pins = []
def pin(name, cond, detail=""):
    pins.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name +
          (f"  [{detail}]" if detail and not cond else ""))

pin("boot alive (the scene game steps immediately — no esc, esc quits)",
    alive)
pin(f"the descent crossed: the wire receipt 'welcome to {DEST}' (the goal "
    "touched, pendingNext consumed, the load spoken)",
    scene is not None and hop_hit(scene, DEST))
events = re.findall(rb"EVENT respawn\([^)]*\) ([^\n]*)", tr)
pin("every fall death named its spawn honestly",
    all(re.search(rb"-> -?\d+,-?\d+\s*$", e) for e in events))
pin("every respawn is the honest fall voice (no ghost states)",
    all(b"respawn(ouch" in m.group(0)
        for m in re.finditer(rb"EVENT respawn[^\n]*", tr)))
pin("the clock stayed honest through the whole walk (pi=0 — no pause "
    "was ever taken)",
    b"pi=0.00" in tr and b"pi=0.01" not in tr and b"pi=0.1" not in tr)
pin("the flood keeps flowing after the receipt", drainf(0.6))
pin("the walk stayed affordable (the honest deaths bounded — a law "
    "churning respawns is a broken law)",
    len(events) <= 60, f"{len(events)} deaths")

try: os.kill(pid, 15)
except Exception: pass
drainf(0.4)
try: os.close(fd)
except Exception: pass
try: os.waitpid(pid, 0)
except Exception: pass
if _os.environ.get("DXN3_L7_DEBUG"):
    _os.system(f"cp {TRACE} /tmp/l7_trace.txt")
if any(not ok for _, ok in pins):
    _fail_trace = f"/tmp/l7_fail_{int(time.time())}.trace"
    try:
        _os.system(f"cp {TRACE} {_fail_trace}")
        print(f"(the failed walk's trace kept at {_fail_trace})")
        import glob as _glob
        _olds = sorted(_glob.glob("/tmp/l7_fail_*.trace"))
        for _o in _olds[:-4]:
            try: os.unlink(_o)
            except Exception: pass
    except Exception:
        pass
try: os.unlink(TRACE)
except Exception: pass

dirty = _os.popen(f"git -C {REPO!r} status --porcelain").read()
pin("the walk wrote nothing (tree snapshot unchanged across the walk)",
    dirty == DIRTY0, dirty[:80])

fails = [n for n, ok in pins if not ok]
print(f"\ndec_level7_probe: {len(pins)-len(fails)}/{len(pins)} pins green "
      f"in {time.time()-t0:.1f}s ({len(events)} honest deaths)")
sys.exit(1 if fails else 0)
