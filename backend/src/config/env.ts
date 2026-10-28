export interface AppBindings {
  DB: D1Database;
  BUCKET: R2Bucket;
  ENVIRONMENT?: string;
}

export const AppConfig = {
  DEFAULT_NOTEBOOK_ID: "default-ielts-notebook",
  DEFAULT_NOTEBOOK_TITLE: "IELTS Mini Practice Tests",
  DEFAULT_NOTEBOOK_DESCRIPTION: "Comprehensive IELTS practice notebook organized into bite-sized Mini-IELTS test cells.",
  MAX_SNAPSHOTS_KEPT: 25,
  AUTO_SYNC_SNAPSHOT_THROTTLE_MS: 20000,
} as const;
