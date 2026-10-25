Rails.application.routes.draw do
  get "up" => "rails/health#show", as: :rails_health_check

  namespace :api do
    namespace :v1 do
      get "health", to: "health#index"

      resources :notebooks do
        member do
          put :sync
          get :export
        end
        collection do
          post :import
          get :current
        end

        resources :snapshots, only: [:index, :show] do
          member do
            post :restore
          end
        end
      end
    end
  end
end
