# Animatrix Assignment Report

## Part 1: Critical Analysis of AI-Generated Code

###  Task 1: Visualization of the Pythagorean Theorem

1. **Issue:** Geometric Coordinate Overlap / Clipping.
   * **Why it matters:** The model generated squares on sides $a$ and $b$ using hardcoded shifts that caused them to clip over the internal boundaries of the central right triangle, completely ruining the geometric proof layout.
   * **How to fix it:** Use structural mathematical vectors relative to the triangle's vertices (e.g., perpendicular vectors out from each side line) instead of static coordinate guessing.

2. **Issue:** Static Label Detachment.
   * **Why it matters:** The labels ($a$, $b$, $c$) were placed at static coordinate positions instead of tracking the midpoints of the lines. If the camera shifts or the layout is scaled, the text completely detaches from the triangle sides.
   * **How to fix it:** Anchor the labels dynamically using `label.next_to(line, direction)` or track them directly to the lines' mathematical midpoints.

3. **Issue:** Compressed / Rushed Timing Logic.
   * **Why it matters:** The AI omitted or used single-second `.wait()` calls between drawing the individual sides and squares. The entire animation flashes on screen almost instantly, making it impossible for a student to follow the sequence.
   * **How to fix it:** Add strategic `self.wait(1.5)` pauses immediately after each structural milestone (drawing the triangle, creating the square areas, and displaying the equation).

4. **Issue:** Lack of Color Hierarchy.
   * **Why it matters:** The squares built on sides $a$ and $b$ used random, unrelated colors that did not visually map to or blend into the color of the hypotenuse square $c$, violating the visual premise that Area $A$ + Area $B$ = Area $C$.
   * **How to fix it:** Implement a strict color palette where Square A (e.g., Red) and Square B (e.g., Yellow) visually combine their identities or color logic into Square C (e.g., Orange).

5. **Issue:** Hardcoded Title Layout Overflow.
   * **Why it matters:** The title text and the algebraic identity ($a^2+b^2=c^2$) were hardcoded around the central origin position `(0,0)`, causing the animated shapes to collide with the text layout.
   * **How to fix it:** Use screen-edge constraints like `.to_edge(UP)` for titles and `.to_edge(DOWN)` for algebraic identifiers to safeguard the viewport canvas.

---

### 🌊 Task 2: Visualization of Fourier Series Decomposition

1. **Issue:** Wave Amplitude Scaling Errors.
   * **Why it matters:** The model plotted subsequent harmonic components with a flat unscaled amplitude (like standard sine waves) instead of mathematically dampening them by a factor of $\frac{4}{\pi \cdot n}$ for each subsequent odd harmonic, failing the fundamental definition of a square wave.
   * **How to fix it:** Correct the wave plotting loop formula to multiply each sine function by `(4.0 / (np.pi * n))`.

2. **Issue:** Axis Range Frame Mismatch.
   * **Why it matters:** The bounding limits for the coordinate axes grid were locked between `-3` and `3`, but the cumulative wave peaks dynamically overflowed past the top and bottom borders because the grid didn't scale with the data.
   * **How to fix it:** Explicitly expand the `y_range` parameters inside the `Axes` configuration block to safely containerize the cumulative wave heights.

3. **Issue:** Overlapping / Smudged Dynamic Text Labels.
   * **How it matters:** As the counter tracked the addition of terms ($n=1, 3, 5...$), the text values were drawn on top of each other at identical pixel coordinates, turning the frame into an unreadable inkblot.
   * **How to fix it:** Wrap the label updating cycle in a clean `Transform(previous_label, new_label)` animation or execute a discrete `FadeOut` of the old label before drawing the next one.

4. **Issue:** Deprecated Palettes & Invalid Keywords.
   * **Why it matters:** The AI attempted to use obsolete or non-existent Manim color handles (like `ORANGE_D`), which causes a strict execution error in modern Manim environments.
   * **How to fix it:** Restrict color selections to standard core Manim constants (`RED`, `ORANGE`, `YELLOW`, `GREEN`, `PURPLE`).

5. **Issue:** Static Frequency Multipliers.
   * **Why it matters:** The frequency variable inside the sine term did not increment alongside the harmonic order index, meaning all 5 waves rendered at the exact same period instead of showing tighter, higher frequencies.
   * **How to fix it:** Ensure the math function multiplies the spatial step count variable by the actual changing harmonic multiplier: `np.sin(n * x)`.


