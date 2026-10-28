import type { FileUploadResponseDto } from "../dto/StorageDto.ts";

export class StorageService {
  constructor(private readonly bucket: R2Bucket) {}

  async uploadFile(file: File): Promise<FileUploadResponseDto> {
    const sanitizedName = file.name.replace(/[^a-zA-Z0-9._-]/g, "_");
    const key = `uploads/${Date.now()}-${crypto.randomUUID().slice(0, 8)}_${sanitizedName}`;
    const arrayBuffer = await file.arrayBuffer();

    await this.bucket.put(key, arrayBuffer, {
      httpMetadata: {
        contentType: file.type || "application/octet-stream",
      },
      customMetadata: {
        originalName: file.name,
        uploadedAt: new Date().toISOString(),
      },
    });

    return {
      success: true,
      key,
      url: `/api/v1/files/${key}`,
      name: file.name,
      type: file.type || "application/octet-stream",
      size: file.size,
    };
  }

  async uploadBinary(
    arrayBuffer: ArrayBuffer,
    customFilename = "unnamed_asset.bin",
    mimeType = "application/octet-stream"
  ): Promise<FileUploadResponseDto> {
    const sanitizedName = customFilename.replace(/[^a-zA-Z0-9._-]/g, "_");
    const key = `uploads/${Date.now()}-${crypto.randomUUID().slice(0, 8)}_${sanitizedName}`;

    await this.bucket.put(key, arrayBuffer, {
      httpMetadata: {
        contentType: mimeType,
      },
      customMetadata: {
        originalName: customFilename,
        uploadedAt: new Date().toISOString(),
      },
    });

    return {
      success: true,
      key,
      url: `/api/v1/files/${key}`,
      name: customFilename,
      type: mimeType,
      size: arrayBuffer.byteLength,
    };
  }

  async getFile(key: string): Promise<R2ObjectBody | null> {
    return this.bucket.get(key);
  }

  async deleteFile(key: string): Promise<void> {
    await this.bucket.delete(key);
  }
}
