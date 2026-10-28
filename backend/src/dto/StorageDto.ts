export interface FileUploadResponseDto {
  success: boolean;
  key: string;
  url: string;
  name: string;
  type: string;
  size: number;
}
