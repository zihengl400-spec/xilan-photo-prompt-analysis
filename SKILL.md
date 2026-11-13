---
name: xilan-photo-prompt-analysis
description: 西兰公园照片提示词分析与生成：分析参考图、生成并对比优化，再用用户上传的本人照片和完整提示词生成同款。明确要求只分析时仅输出文字。
---

# Xilan Photo Prompt Analysis

## Contract

Use Chinese for all user-facing output. Default to a complete per-photo workflow in Doubao Agent: inspect reference → write full prompt → generate version 1 → inspect and compare → rewrite full prompt → generate version 2 → deliver → wait for the user’s personal photo → generate their version. A normal request to use this skill with photos authorizes this bounded workflow; proceed between stages without asking the user to upload results that you already have or approve each step. Installation alone does not start generation. Honor explicit “只分析”, “不要生成图片” or equivalent instructions: run only the requested textual analysis/comparison and skip generation. Do not modify the photo-template repository or publish user photos.

## Target generation model

Use Doubao Agent's available image-generation tool with the explicitly identified model **Seedream 5.5**, not Seedream 5.0 Pro, 5.0 Flash, or another version. Before the first generation, verify the actual tool/model availability from exposed tool metadata or the model selector. A model name in a prompt is not model selection. Do not invent tool parameters, model IDs, capabilities or availability. If the exact model cannot be selected or verified, stop generation, deliver any completed prompt and state that the required generation capability is unavailable; never silently downgrade or claim success. A user-provided comparison image does not prove which model generated it.

The user need not specify the model on each invocation. Keep model settings out of routine narration and the visual prompt; answer truthfully if asked. Obey actual platform permissions and stop if the platform requires user action. Do not buy credits or change subscriptions. No fallback to external image services.

For the reference-analysis stage, default to **text-to-image** so the generated result tests the prompt's reconstruction quality. Pass the complete validated prompt unchanged, with supported portrait 3:4 settings, and request one image. Do not attach the reference photo to these two initial text-to-image generations unless the user explicitly requests it. The later personal-photo stage has a separate image-reference rule below. Never truncate the prompt to fit a tool limit: report that limit and stop instead. Keep model, ratio and other supported settings consistent between rounds; reuse a seed only if the tool actually exposes one. Do not invent it.

Read [the complete example](references/full-example.txt) and [the analysis method](references/method.md) before writing. Preserve the example file in full. Follow its depth, narrative structure and causal explanations, but replace its photographic content with evidence from each actual reference. Do not inherit fixed faces, hair, makeup, outfits, props, camera angles, flash, CCD styling, expressions or negative constraints from the example or unrelated skills.

All output prompts use portrait **3:4**. This explicitly overrides the example's original 2:3. If the source has another aspect ratio, describe its observed geometry honestly and adapt the requested 3:4 framing conservatively; do not claim the source itself was 3:4. Do not introduce scene contents to fill space.

## Stage 1 — Analyze each source independently

1. Inspect the actual uploaded images in their supplied order. Assign stable IDs: 原图1, 原图2, etc. A collage is not a single coherent scene: label its panels by position and analyze each independently unless the user specifies otherwise. Do not mix clothes, poses or scenery between sources.
2. When references are accessible, proceed without asking the user to repeat the task. If an image is unreadable or absent, request only that missing image. Do not infer photo content from filenames.
3. Apply the method reference. Internally identify the strongest 3–5 likeness anchors, uncertain details and the source's actual lighting. Write one complete, copyable Chinese prompt per source, beginning “帮我生成图片：” and explicitly specifying “画面比例为纵向3:4”. Use connected detailed paragraphs in the example's order, followed by core keywords and tailored negative constraints. Do not output a short outline or just a tag list.
4. Save each prompt as UTF-8 text when file-writing is available, validate its length using the procedure below, and revise before delivering it. Output `原图N｜第一版提示词` followed by the complete prompt. Keep filenames/IDs unambiguous. Do not replace inline prompts with summaries; a downloadable full text is supplementary.
5. For batches, complete the entire two-round workflow for one photo before moving to the next. Preserve source IDs across prompts, generated images and comparison records. Never mix sources, truncate a prompt or claim unfinished photos are done. If a platform limit interrupts the batch, report completed and pending IDs and preserve progress.
6. In analysis-only mode, deliver the complete prompt and stop. Otherwise continue immediately to first generation.

## First generation

Submit the complete first prompt through the verified tool and wait for its actual result. If the tool returns a job ID, follow that existing job instead of resubmitting. Preserve the image/result ID and the exact submitted prompt under `原图N / 第一版`. Inspect the returned image with the available image-viewing capability; a completion message or URL alone is not visual evidence. If generation fails or the result cannot be viewed, report the failure and stop this photo's workflow; do not invent a comparison. Do not automatically resubmit a failed or uncertain job. If the model is unavailable globally, stop the batch rather than repeating failed requests.

Once version 1 is available and visible, automatically pair the original reference as 图1 and version 1 as 图2, then continue to comparison. Do not ask the user to upload these same images again.

## Stage 2 — Compare and rewrite

This stage runs automatically after first generation. It can also be entered directly when the user supplies a reference/generated pair. Default **图1 = reference, 图2 = generated**, honoring explicit labels over order. With multiple pairs or ambiguous roles, clarify their mapping before comparing. Access both images, not just the generated result. Reuse the matching first-stage prompt if available; if it is missing, explain that you can rewrite from the pair but cannot identify the exact wording that caused the error. An explicit analysis-only request produces comparison and revised text without generation.

Read [the original comparison instruction](references/comparison.txt). Compare all ten requested dimensions: clothing; makeup and hair; body pose and placement; color; facial micro-expression; background; flash and lighting; overall feeling; composition and occupancy; object positions. Mark unchanged or unobservable dimensions honestly. Use a compact table with reference evidence, generated deviation and actionable prompt correction. State approximate ratios only as visual estimates, not measurements. Diagnose effects visible in the images; potential prompt causes are hypotheses.

Prioritize the 3–5 highest-impact differences. Preserve successful traits while correcting deviations. Rebuild the entire prompt, integrating corrections into the relevant paragraphs. Resolve contradictions and update the negative constraints; do not append conflicting instructions to an unchanged draft. Match the full-example length target again; do not give only a patch, “same as above”, or omit sections. Output `对比分析` followed by `完整优化提示词（第二版）` and the full self-contained prompt. Validate the revised text before the second generation.

## Second generation and delivery

Unless the user requested analysis only, submit the complete revised prompt to the same verified model with the same supported settings. Generate one second-version image and inspect the actual result. Deliver the original reference, version 1 and version 2 with clear labels, the full final prompt, the comparison and a brief evidence-based assessment of improvements and remaining differences. Provide native image previews and usable download links/files when supported. Save full prompts as UTF-8 text when possible; do not claim saved artifacts without actually writing them. If version 2 is worse in some respects, say so rather than declaring automatic success.

Stop after these **two generation requests per source**. Do not enter an unlimited generate/compare loop or silently generate extra candidates. If the user supplied version 1, only one new request is needed for version 2. A second-round failure returns the completed first image, revised prompt and truthful failure status. After these two reference-stage requests, invite the user to upload their own photo and wait. The later personal-photo generation is a separate request explicitly triggered by the user’s photo and request. Further reference-stage iterations require a new request. Installation, analysis-only and comparison-only requests do not trigger unrequested generation.

## Stage 3 — Personal photo and selected prompt

After the reference stage, ask the user to upload their own photo and say “用我的照片做同款”. Do not assume the reference photo is their personal photo or reuse a generated image as an identity reference. When the user supplies their photo and requests the same look, use the **full second-version prompt** associated with the selected reference as the default; use version 1 only when the user explicitly chooses it. If multiple reference images or prompt versions could apply and the selection is unclear, ask which reference/version; do not silently guess. Preserve the chosen prompt in full and append this exact paragraph without changing it:

请优先保留上传照片中的真实人物身份特征，尤其保留脸型轮廓、眼型、眼距、鼻梁、鼻头、唇形、下颌线、面部留白、发际线、刘海状态与整体神态辨识度。最终生成结果必须让人一眼看出与上传照片为同一人，而不是仅保留大致气质。姿势可以不一样。

The personal image is the **only image supplied as the identity reference** to the image generation tool. The original reference image and generated examples are for visual analysis and comparison, not inputs to a direct reference-plus-person face swap. Submit the complete selected prompt plus the exact paragraph and personal photo to the verified Seedream 5.5 tool as an image-guided request. Person-specific appearance, hairline and fringe from the personal photo take precedence over conflicting identity or hairline/fringe descriptions of the original reference; the original prompt still supplies composition, clothing, light, scene and mood where compatible. Do not silently discard other prompt sections or claim guaranteed identity accuracy. The user can explicitly request a different pose; otherwise use the reference prompt’s pose as the target.

Request one personal result, inspect it if supported, present the actual image with the exact complete submitted text or a complete downloadable text file, and report any visible identity mismatch honestly. If the tool cannot accept a photo plus the complete prompt, or the required model cannot be verified, explain the limitation and stop; do not replace the model or perform a face swap. A failed or uncertain job must not be resubmitted automatically. Do not upload personal photos to GitHub. A user's additional request is required for another personal generation.

The ±200-character constraint applies to each complete reference-stage prompt before this personal identity paragraph is appended. Preserve both the full validated prompt and the exact appended paragraph; report combined length separately if measured. Do not shorten the original prompt to accommodate the paragraph.

## Length requirement

The canonical baseline is the entire `references/full-example.txt`, from “帮我生成图片：” to the final ratio, including keywords and negative constraints but excluding the surrounding user's explanation. Count Unicode non-whitespace characters, including punctuation, digits and Latin characters; exclude headings, Markdown fences, comparison tables and delivery notes from candidate files. This is the defined “字数” convention for this skill.

Every first and revised prompt must be within **baseline ±200 characters**, inclusive; this target stays fixed across revisions. Do not shorten the canonical example, reset the baseline to a shorter draft, or count the comparison analysis toward it. Use the Python standard-library checker when available:

`python scripts/check_length.py path/to/prompt.txt [path/to/another-prompt.txt ...]`

The checker reads the bundled baseline and exits nonzero on any failure. An equivalent local Unicode-aware counter is acceptable if Python is unavailable. If no execution/counting tool is available, say `字数未程序校验` rather than claiming verified compliance. Aim near the baseline, not its lower bound. Do not invent details or repeat empty adjectives to meet length: expand visible spatial relationships, color roles, material/light interactions and reconstruction priorities instead. If the reference is too sparse or unreadable to support the required detail, disclose that conflict and ask for a clearer reference or a relaxed length constraint.

## Final review

Before delivery check: correct image mapping; 3:4 throughout; no carried-over example scene; no invented hidden details or fixed-person appearance; makeup and expression analyzed distinctly; consistent lighting direction and exposure; spatial estimates internally consistent; tailored negative constraints; complete standalone prompts; length validated or limitation disclosed; verified model selection for actual generation; no generation in analysis-only mode; at most two reference-stage generation requests per source and one explicitly requested personal-photo generation; actual results inspected before comparison; accurate progress and artifact links. Describe observable results, not guaranteed pixel-perfect reproduction.
