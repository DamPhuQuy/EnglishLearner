import { BarChart3, Eye, FileSpreadsheet, GitBranch, MapPin, PieChart, TrendingUp } from "lucide-react";
import React, { useState } from "react";
import type { IeltsWritingTaskData } from "../../types/ieltsSchema.ts";

export interface AcademicVisualStimulusProps {
  writingTask: IeltsWritingTaskData;
  imageUrl?: string;
  imageDescription?: string;
}

export const AcademicVisualStimulus: React.FC<AcademicVisualStimulusProps> = ({
  writingTask,
  imageUrl,
  imageDescription,
}) => {
  const [showDescription, setShowDescription] = useState(false);
  const visualType = writingTask.academicVisualType || "bar_chart";

  const getVisualIcon = () => {
    switch (visualType) {
      case "line_graph":
        return <TrendingUp size={15} className="text-cyan-400" />;
      case "pie_chart":
        return <PieChart size={15} className="text-amber-400" />;
      case "table":
        return <FileSpreadsheet size={15} className="text-emerald-400" />;
      case "map_plan":
        return <MapPin size={15} className="text-rose-400" />;
      case "process_diagram":
        return <GitBranch size={15} className="text-purple-400" />;
      default:
        return <BarChart3 size={15} className="text-blue-400" />;
    }
  };

  const getVisualLabel = () => {
    return visualType
      .replace(/_/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase());
  };

  return (
    <div className="academic-visual-container border border-slate-700/80 rounded-xl bg-slate-900/90 overflow-hidden my-3 shadow-md">
      {/* Top Header */}
      <div className="flex items-center justify-between px-3.5 py-2.5 bg-slate-800/70 border-b border-slate-700/60">
        <div className="flex items-center gap-2">
          {getVisualIcon()}
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-200">
            {getVisualLabel()} Visual Stimulus
          </span>
        </div>
        {imageDescription && (
          <button
            type="button"
            onClick={() => setShowDescription((v) => !v)}
            className="flex items-center gap-1.5 px-2 py-1 text-xs font-medium text-slate-300 hover:text-white bg-slate-700/50 hover:bg-slate-700 rounded transition"
            title="Toggle accessible text description of chart data"
          >
            <Eye size={12} />
            <span>{showDescription ? "Hide Data Table" : "View Data Details"}</span>
          </button>
        )}
      </div>

      {/* Visual Stimulus Area */}
      <div className="p-3 flex flex-col items-center justify-center bg-slate-950/60">
        {imageUrl ? (
          <div className="w-full flex justify-center overflow-x-auto py-1">
            <img
              src={imageUrl}
              alt={imageDescription || `${getVisualLabel()} diagram`}
              className="max-h-[380px] w-auto object-contain rounded-lg border border-slate-800 shadow"
            />
          </div>
        ) : (
          <div className="text-center py-6 text-slate-400 text-sm">
            <BarChart3 size={28} className="mx-auto mb-2 text-slate-500 opacity-60" />
            <p>Visual diagram stimulus ready</p>
          </div>
        )}

        {/* Accessible Data Description Drawer */}
        {showDescription && imageDescription && (
          <div className="w-full mt-3 p-3 bg-slate-800/90 border border-slate-700 rounded-lg text-xs leading-relaxed text-slate-300">
            <strong className="block text-slate-100 font-semibold mb-1">
              Data Breakdown & Key Measurements:
            </strong>
            <p className="whitespace-pre-line">{imageDescription}</p>
          </div>
        )}
      </div>
    </div>
  );
};
