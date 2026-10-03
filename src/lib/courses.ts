import fs from 'node:fs';
import path from 'node:path';
import { parse } from 'yaml';

export interface LocalizedText {
	en: string;
	es?: string;
}

export interface CoursePath {
	id: string;
	label: LocalizedText;
}

export interface Course {
	slug: string;
	status: 'draft' | 'published';
	title: LocalizedText;
	subtitle: LocalizedText;
	paths: CoursePath[];
}

const COURSES_DIR = path.resolve(process.cwd(), 'courses');

export function getCourses(): Course[] {
	return fs
		.readdirSync(COURSES_DIR, { withFileTypes: true })
		.filter((entry) => entry.isDirectory())
		.map((entry) => {
			const file = path.join(COURSES_DIR, entry.name, 'course.yml');
			return parse(fs.readFileSync(file, 'utf-8')) as Course;
		});
}

export function localize(
	text: LocalizedText,
	locale: string | undefined,
): string {
	if (locale === 'es' && text.es) return text.es;
	return text.en;
}
