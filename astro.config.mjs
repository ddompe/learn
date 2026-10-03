// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightLinksValidator from 'starlight-links-validator';

// https://astro.build/config
export default defineConfig({
	site: 'https://learn.dompe.space',
	integrations: [
		starlight({
			title: { en: "Let's learn together", es: 'Aprendamos juntos' },
			defaultLocale: 'en',
			locales: {
				en: { label: 'English', lang: 'en' },
				es: { label: 'Español', lang: 'es' },
			},
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/ddompe/learn',
				},
			],
			plugins: [starlightLinksValidator()],
			components: {
				Footer: './src/components/Footer.astro',
			},
			head: [
				// Remembers the locale of the last page visited, read by the root
				// language-detection redirect at src/pages/index.astro.
				{
					tag: 'script',
					content:
						"localStorage.setItem('preferredLocale', document.documentElement.lang)",
				},
				{
					tag: 'script',
					attrs: {
						'data-goatcounter': 'https://ddompe.goatcounter.com/count',
						async: true,
						src: '//gc.zgo.at/count.js',
					},
				},
			],
			sidebar: [
				{
					label: 'Automation & AI for Business Users',
					translations: { es: 'Automatización e IA para profesionales' },
					items: [
						{
							label: 'Course home',
							translations: { es: 'Inicio del curso' },
							link: '/automation-ai/',
						},
						{
							label: 'Part 0 — Orientation',
							translations: { es: 'Parte 0 — Orientación' },
							items: [
								{ autogenerate: { directory: 'automation-ai/00-orientation' } },
							],
						},
						{
							label: 'Part 1 — Computer fundamentals',
							translations: { es: 'Parte 1 — Fundamentos de computación' },
							items: [
								{
									autogenerate: {
										directory: 'automation-ai/01-computer-fundamentals',
									},
								},
							],
						},
						{
							label: 'Part 2 — LLMs demystified',
							translations: { es: 'Parte 2 — Los LLM al descubierto' },
							items: [
								{
									autogenerate: {
										directory: 'automation-ai/02-llms-demystified',
									},
								},
							],
						},
						{
							label: 'Part 3 — Software engineering fundamentals',
							translations: {
								es: 'Parte 3 — Fundamentos de ingeniería de software',
							},
							items: [
								{
									autogenerate: {
										directory: 'automation-ai/03-software-engineering',
									},
								},
							],
						},
						{
							label: 'Part 4 — Python foundations',
							translations: { es: 'Parte 4 — Fundamentos de Python' },
							items: [
								{
									autogenerate: {
										directory: 'automation-ai/04-python-foundations',
									},
								},
							],
						},
						{
							label: 'Part 5 — Data formats',
							translations: { es: 'Parte 5 — Formatos de datos' },
							items: [
								{
									autogenerate: { directory: 'automation-ai/05-data-formats' },
								},
							],
						},
						{
							label: 'Part 6 — Business data with Python',
							translations: { es: 'Parte 6 — Datos de negocio con Python' },
							items: [
								{
									autogenerate: { directory: 'automation-ai/06-business-data' },
								},
							],
						},
						{
							label: 'Part 7 — Visualization',
							translations: { es: 'Parte 7 — Visualización' },
							items: [
								{
									autogenerate: { directory: 'automation-ai/07-visualization' },
								},
							],
						},
						{
							label: 'Part 8 — Documentation and reports',
							translations: { es: 'Parte 8 — Documentación e informes' },
							items: [
								{
									autogenerate: {
										directory: 'automation-ai/08-documentation-reports',
									},
								},
							],
						},
						{
							label: 'Part 9 — Automation and capstone',
							translations: { es: 'Parte 9 — Automatización y proyecto final' },
							items: [
								{
									autogenerate: {
										directory: 'automation-ai/09-automation-capstone',
									},
								},
							],
						},
						{
							label: 'Part 10 — Advanced: LLMs from code',
							translations: { es: 'Parte 10 — Avanzado: LLM desde código' },
							items: [
								{
									autogenerate: { directory: 'automation-ai/10-advanced-llms' },
								},
							],
						},
					],
				},
			],
		}),
	],
});
