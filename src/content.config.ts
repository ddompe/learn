import { defineCollection } from 'astro:content';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';
import { z } from 'astro/zod';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				lessonId: z.string().optional(),
				estimatedMinutes: z.number().optional(),
				prerequisites: z.array(z.string()).default([]),
				lastVerified: z.coerce.date().optional(),
				sourceHash: z.string().optional(),
				translationStatus: z.enum(['machine', 'reviewed']).optional(),
			}),
		}),
	}),
	i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
};
