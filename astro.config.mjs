// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { satteri } from '@astrojs/markdown-satteri';
import fs from 'node:fs';

// Mismos ids de encabezado que generaba mkdocs (toc.slugify): sin tildes.
// Así siguen funcionando los #anclas enlazados desde afuera y entre guías.
// Corre antes del plugin de ids de Astro, que respeta los ids ya puestos.
const mkdocsSlugs = () => {
	const seen = new Map();
	return {
		name: 'mkdocs-slugs',
		element: {
			filter: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
			visit(node, ctx) {
				if (typeof node.properties?.id === 'string') return;
				let id = ctx.textContent(node).normalize('NFKD').replace(/[^\x00-\x7F]/g, '')
					.replace(/[^\w\s-]/g, '').trim().toLowerCase().replace(/[-\s]+/g, '-');
				const k = seen.get(id) ?? 0;
				seen.set(id, k + 1);
				ctx.setProperty(node, 'id', k ? `${id}_${k}` : id);
			},
		},
	};
};

const legacy = {
	guia_abiertos: 'guia-abiertos',
	guia_interoperables: 'guia-interoperables',
	guia_metadatos: 'guia-metadatos',
	guia_apn: 'guia-apn',
	guia_subnacionales: 'guia-subnacionales',
	perfil_metadatos: 'perfil-metadatos',
	'datasets-especificaciones': 'datasets-sugeridos',
};
const base = '/paquete-apertura-datos';

export default defineConfig({
	site: 'https://datosgobar.github.io',
	base,
	trailingSlash: 'ignore',
	markdown: { processor: satteri({ hastPlugins: [mkdocsSlugs] }) },
	redirects: {
		// Astro no antepone `base` al destino.
		...Object.fromEntries(Object.entries(legacy).map(([a, b]) => [`/${a}/`, `${base}/${b}/`])),
		...Object.fromEntries(fs.readdirSync('src/content/docs/datasets-sugeridos').map((f) => f.replace('.md', '')).map((slug) => [`/datasets-especificaciones/${slug}/`, `${base}/datasets-sugeridos/${slug}/`])),
		// Especificación vacía en mkdocs (solo el título): no se migró.
		'/datasets-especificaciones/presupuesto-ingresos/': `${base}/datasets-sugeridos/`,
	},
	integrations: [
		starlight({
			title: 'Paquete de Apertura de Datos',
			description: 'Guías y recursos para la apertura de datos públicos nacionales y subnacionales en Argentina.',
			defaultLocale: 'root',
			locales: { root: { label: 'Español', lang: 'es' } },
			favicon: '/assets/images/favicon.png',
			customCss: ['./src/styles/datos.css', './src/styles/hub.css'],
			components: { Hero: './src/components/Hero.astro', Header: './src/components/Cabecera.astro' },
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/datosgobar/paquete-apertura-datos' }],
			editLink: { baseUrl: 'https://github.com/datosgobar/paquete-apertura-datos/edit/master/' },
			head: [
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
				{ tag: 'link', attrs: { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap' } },
				// ponytail: un solo diagrama en todo el sitio; mermaid se carga solo si la página lo tiene.
				{ tag: 'script', attrs: { type: 'module' }, content: "if (document.querySelector('pre.mermaid')) { const { default: m } = await import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'); m.initialize({ startOnLoad: false, theme: document.documentElement.dataset.theme === 'dark' ? 'dark' : 'neutral' }); m.run(); }" },
				{ tag: 'script', attrs: { async: true, src: 'https://www.googletagmanager.com/gtag/js?id=G-WFY4MZM8FP' } },
				{ tag: 'script', content: "window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-WFY4MZM8FP');" },
			],
			// Mismo menú y mismos nombres que el nav de mkdocs.yml.
			sidebar: [
				{ label: 'Inicio', link: '/' },
				{ label: 'Empezar', slug: 'empezar' },
				{
					label: 'Guías de buenas prácticas',
					items: [
						{ label: 'Guía para la publicación de datos en formatos abiertos', slug: 'guia-abiertos' },
						{ label: 'Guía para la identificación y uso de entidades interoperables', slug: 'guia-interoperables' },
						{ label: 'Guía para el uso y la publicación de metadatos', slug: 'guia-metadatos' },
						{ label: 'Datasets sugeridos', slug: 'datasets-sugeridos' },
					],
				},
				{
					label: 'Guías de implementación',
					items: [
						{ label: 'Guía para la apertura de datos en organismos de la Administración Pública Nacional', slug: 'guia-apn' },
						{ label: 'Guía para la apertura de datos en gobiernos provinciales y locales', slug: 'guia-subnacionales' },
					],
				},
				{
					label: 'Marco legal',
					items: [
						{ label: 'Decreto 117/2016 "Plan de Apertura de Datos"', slug: 'decreto-117-2016' },
						{ label: 'Ley 27275 "Derecho de Acceso a la Información Pública"', slug: 'ley-27275-2016' },
						{ label: 'Perfil de Aplicación Nacional de Metadatos para Datos Abiertos', slug: 'perfil-metadatos' },
					],
				},
				{ label: 'Herramientas', slug: 'herramientas' },
				{ label: 'Glosario', slug: 'glosario' },
				{
					label: 'Anexos',
					items: [
						{ label: 'Anexo I - Perfil de Aplicación Nacional de Metadatos para Datos Abiertos (PDF)', link: '/pdf/anexo-I-perfil-metadatos.pdf', attrs: { target: '_blank', rel: 'noopener' } },
						{ label: 'Anexo II - Guía para la publicación de datos en formatos abiertos (PDF)', link: '/pdf/anexo-II-guia-abiertos.pdf', attrs: { target: '_blank', rel: 'noopener' } },
						{ label: 'Anexo III - Guía para la identificación y uso de entidades interoperables (PDF)', link: '/pdf/anexo-III-guia-interoperables.pdf', attrs: { target: '_blank', rel: 'noopener' } },
					],
				},
			],
		}),
	],
});
